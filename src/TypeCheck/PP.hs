{-# LANGUAGE RecordWildCards #-}

module TypeCheck.PP where

import Scope.Name
import TypeCheck.AST

import qualified Data.Foldable as F
import qualified Data.Text.Lazy as L
import           Text.PrettyPrint.HughesPJ


pp :: PP a => a -> Doc
pp  = ppPrec 0

optParens :: Bool -> Doc -> Doc
optParens True  = parens
optParens False = id

class PP a where
  ppPrec :: Int -> a -> Doc

  ppList :: [a] -> Doc
  ppList as = brackets (fsep (punctuate comma (map pp as)))

instance PP Int where
  ppPrec _ = int

instance PP Char where
  ppPrec _ = char
  ppList   = text

instance PP L.Text where
  ppPrec _ = text . L.unpack

instance PP Name where
  ppPrec _ = pp . nameText

instance PP Integer where
  ppPrec _ = integer

instance PP Controller where
  ppPrec _ Controller { .. } =
    vcat $ [ text "controller" <+> pp cName <+> text "where" ]
        ++ map pp cEnums
        ++ concatMap (map pp . F.toList) cFuns
        ++ map (ppStateVar "input")  cInputs
        ++ map (ppStateVar "output") cOutputs
        ++ [ hang (text "env_trans")    2 (pp cEnvTrans)
           , hang (text "env_liveness") 2 (pp cEnvLiveness)
           , hang (text "sys_trans")    2 (pp cSysTrans)
           , hang (text "sys_liveness") 2 (pp cSysLiveness) ]

ppStateVar :: String -> StateVar -> Doc
ppStateVar lab StateVar { .. } =
  hang (text lab <+> pp svName <+> char ':' <+> pp svType)
     2 (maybe empty pp svInit)

instance PP Fun where
  ppPrec _ Fun { .. } =
    hang (text fName
          <+> parens (fsep (punctuate comma (map ppParam fParams)))
          <> colon
          <+> pp fResult
          <+> char '=')
       2 (pp fBody)
    where
    ppParam (p,ty) = pp p <> colon <+> pp ty

instance PP Expr where
  ppPrec _ ETrue      = text "True"
  ppPrec _ EFalse     = text "False"
  ppPrec _ (EVar n)   = pp n
  ppPrec _ (ECon n)   = pp n
  ppPrec _ (ENum i)   = pp i
  ppPrec p (EAnd l r) = ppBinop p l (text "&&") r
  ppPrec p (EOr  l r) = ppBinop p l (text "||") r
  ppPrec p (EEq l r)  = ppBinop p l (text "=")  r
  ppPrec p (ENot a)   = optParens (p >= 10) (text "!" <+> ppPrec 10 a)
  ppPrec p (EApp f x) = optParens (p >= 10) (hang (pp f) 2 (ppPrec 10 x))
  ppPrec _ (ENext e)  = char 'X' <> parens (pp e)

ppBinop :: (PP a, PP b) => Int -> a -> Doc -> b -> Doc
ppBinop p a x b = optParens (p >= 10) (sep [ppPrec 10 a, x, ppPrec 10 b])

instance PP Type where
  ppPrec _ (TFree v)  = char '?' <> pp v
  ppPrec _ TBool      = text "Bool"
  ppPrec _ TInt       = text "Num"
  ppPrec _ (TEnum n)  = pp n
  ppPrec p (TFun a b) = optParens (p >= 10) (sep [ ppPrec a 10 <+> text "->", pp b ])
