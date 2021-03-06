module Slugs (
    runSlugs,
    parseSlugsJSON,
    parseSlugsOut,
    FSM(..),
    Node(..),
  ) where

import Slugs.FSM (fromSlugs,fromSlugs',FSM(..),Node(..))
import Slugs.Translate (mkSpec)
import TypeCheck.AST (Controller)

import           Control.Monad (when)
import qualified Data.ByteString.Lazy as L
import qualified Language.Slugs as S


runSlugs :: Bool -> FilePath -> FilePath -> Controller -> IO (Maybe FSM)
runSlugs dbg z3Prog slugsProg cont =
  do let (spec,env) = mkSpec cont
         spec' = S.simpSpec spec

     when dbg $
       do putStrLn "-- unoptimized --------------------------------"
          print (S.ppSpec spec)
          putStrLn ""
          putStrLn "-- optimized ----------------------------------"
          print (S.ppSpec spec')

     res <- S.runSlugs dbg slugsProg spec'
     case res of
       S.Unrealizable{}  -> return Nothing
       S.StateMachine sm -> fromSlugs dbg z3Prog env cont sm


parseSlugsJSON :: FilePath -> Int -> L.ByteString -> Maybe FSM
parseSlugsJSON path numInputs input = fromSlugs' path numInputs `fmap` S.fsmFromJSON input

parseSlugsOut :: FilePath -> Int -> L.ByteString -> Maybe FSM
parseSlugsOut path numInputs input = fromSlugs' path numInputs `fmap` S.parseSlugsOut input
