{-# LANGUAGE RecordWildCards #-}
{-# LANGUAGE OverloadedStrings #-}

import Options

import           CodeGen.Dot (dotFSM)
import           CodeGen.Java (Package,javaFSM)
import           CodeGen.Python (pythonFSM)
import           Message (ppError)
import           Opt (opt)
import           Opt.Simpl (simp)
import           PP (Doc,pp,text)
import           Scope.Check
import           Scope.Name (Name,emptySupply,nameText)
import           Slugs (runSlugs,parseSlugsJSON,parseSlugsOut,FSM)
import           Syntax.AST
import           Syntax.Parser
import           TypeCheck
import qualified TypeCheck.AST as TC

import           Control.Exception (catch,IOException)
import           Control.Monad (when)
import qualified Data.Aeson as JSON
import qualified Data.Aeson.Encode.Pretty as JSON
import qualified Data.ByteString.Lazy.Char8 as LB
import qualified Data.Foldable as F
import qualified Data.Map.Strict as Map
import           Data.Maybe (mapMaybe)
import qualified Data.Text.IO as T
import           System.Directory (createDirectoryIfMissing)
import           System.Exit (exitFailure)
import           System.FilePath (takeDirectory,(</>))
import           System.IO (hPrint,stderr)
import           Text.Show.Pretty (ppShow)

main :: IO ()
main  =
  do opts <- parseOptions

     input <-
       case optInput opts of
         Just inp -> return inp
         Nothing  -> do putStrLn "No input specified"
                        exitFailure

     fsm <- genFSM opts input

     case optJava opts of
       Just pkg -> writePackage opts (javaFSM pkg fsm)
       Nothing  -> return ()

     when (optPython opts) (writePackage opts (pythonFSM fsm))

     when (optDot opts) (writePackage opts (dotFSM fsm))

genFSM :: Options -> Input -> IO FSM

genFSM opts (InpSpec path) =
  do bytes <- T.readFile path

     pCont <-
       case parseController path bytes of
         Right p  -> return p
         Left err -> do output (ppError err)
                        exitFailure

     when (optDumpParsed opts) (output (text (ppShow pCont)))

     (scCont,scSup) <-
       case scopeCheck emptySupply pCont of
         Right sc  -> return sc
         Left errs -> do mapM_ (output . ppError) errs
                         exitFailure

     (tcCont,tcSup) <-
       case typeCheck scSup scCont of
         Right tc  -> return tc
         Left errs -> do mapM_ (output . ppError) errs
                         exitFailure

     when (optAnnotations opts) (dumpAnnotations tcCont)

     when (optDumpCore opts) (output (pp tcCont))

     let exCont = expand tcCont
     when (optDumpExpanded opts) (output (pp exCont))

     -- sanity check the expanded module
     -- NORE: sanity checking requires that expand has been called.
     sMsgs <- sanityCheck (optDumpSanity opts) (optZ3 opts) exCont
     mapM_ (output . ppSanityMessage) sMsgs
     when (not (null (sanityErrors sMsgs))) exitFailure

     when (optDumpSimp opts) (output (pp (simp exCont)))

     (oCont,_) <-
       if optOptLevel opts >= 1 
          then do let (oCont,oSup) = opt tcSup exCont
                  when (optDumpOpt opts) (output (pp oCont))
                  return (oCont,oSup)

          else return (exCont,tcSup)

     mb <- runSlugs (optDumpSpec opts) (optZ3 opts) (optSlugs opts) oCont `catch` \ e ->
       do let _ = e :: IOException
          putStrLn "Failed to run slugs. Is SLUGS set?"
          exitFailure

     case mb of
       Just fsm -> return fsm
       Nothing  -> do putStrLn "Unrealizable"
                      exitFailure

genFSM opts (InpJSON path) =
  do numInputs <-
       case optInputLen opts of
         Just len -> return len
         Nothing  -> do putStrLn "`--length` flag is required when consuming raw slugs output"
                        exitFailure

     json <- LB.readFile path

     case parseSlugsJSON path numInputs json of
       Just fsm -> return fsm
       Nothing  -> do putStrLn "Failed to parse slugs JSON output"
                      exitFailure

genFSM opts (InpSlugsOut path) =
  do numInputs <-
       case optInputLen opts of
         Just len -> return len
         Nothing  -> do putStrLn "`--length` flag is required when consuming raw slugs output"
                        exitFailure

     slugsout <- LB.readFile path

     case parseSlugsOut path numInputs slugsout of
       Just fsm -> return fsm
       Nothing  -> do putStrLn "Failed to parse slugs output"
                      exitFailure

-- | Used to dump messages and AST to stderr.
output :: Doc -> IO ()
output  = hPrint stderr

-- | Write out a package generated by one of the code generators.
writePackage :: Options -> Package -> IO ()
writePackage opts pkg = mapM_ writeClass (Map.toList pkg)
  where
  prefix = case optOutDir opts of
             Just dir -> dir
             Nothing  -> ""

  writeClass (file,doc) =
    do let outFile = prefix </> file
       putStrLn ("Writing " ++ outFile)
       createDirectoryIfMissing True (takeDirectory outFile)

       writeFile outFile (show doc)


dumpAnnotations :: TC.Controller -> IO ()
dumpAnnotations TC.Controller { .. } =
  LB.putStrLn $ JSON.encodePretty
              $ JSON.toJSON
              $ funs ++ enums ++ stateVars

  where

  funs = mapMaybe dumpFun (concatMap F.toList cFuns)

  dumpFun TC.Fun { .. } =
    do annot <- fAnn
       return $ JSON.object [ "macro"      JSON..= jsonName fName
                            , "annotation" JSON..= jsonAnnotation annot ]

  enums = mapMaybe dumpEnum cEnums

  dumpEnum TC.EnumDef { .. } = 
    do annot <- eAnn
       return $ JSON.object [ "enum"       JSON..= jsonName eName
                            , "annotation" JSON..= jsonAnnotation annot
                            , "values"     JSON..= map jsonName eCons ]
 
  stateVars = mapMaybe (dumpStateVar "input")  cInputs
           ++ mapMaybe (dumpStateVar "output") cOutputs

  dumpStateVar ty = \ TC.StateVar { .. } ->
    do annot <- svAnn
       return $ JSON.object [ ty           JSON..= jsonName svName
                            , "annotation" JSON..= jsonAnnotation annot ]



jsonAnnotation :: Ann Renamed -> JSON.Value
jsonAnnotation  = go
  where
  go (AnnApp _ f xs) =
    JSON.object [ "name" JSON..= f
                , "args" JSON..= map go xs ]

  go (AnnArr _ xs) =
    JSON.toJSON (map go xs)

  go (AnnObj _ xs) =
    JSON.object [ l JSON..= go x | (l,x) <- xs ]

  go (AnnSym _ sym) =
    JSON.toJSON sym

  go (AnnStr _ str) =
    JSON.toJSON str

  go (AnnCode _ ty str) =
    JSON.object [ "language" JSON..= ty
                , "code"     JSON..= str ]


jsonName :: Name -> JSON.Value
jsonName n = JSON.toJSON (nameText n)
