{-# LANGUAGE RecordWildCards #-}

module Slugs.Env (
    Env(..),
    mkEnv,
    lookupVar,
    lookupConstr,
    lookupEnum,
  ) where

import Scope.Name (Name,nameText,nameUnique)
import TypeCheck.AST (Controller(..),StateVar(..),Type(..),EnumDef(..))

import qualified Data.Map.Strict as Map
import qualified Data.Text.Lazy as T
import qualified Language.Slugs as Slugs


data Env = Env { envEnums   :: Map.Map Name EnumDef
               , envConstrs :: Map.Map Name Int
               , envVars    :: Map.Map Name Slugs.Var
               , envVars'   :: Map.Map String Name
               } deriving (Show)

panic :: String -> a
panic str = error ("PANIC: " ++ str)

-- | Produce an environment, input variables, and output variables, from a
-- controller.
mkEnv :: Controller -> (Env,[Slugs.Var],[Slugs.Var])
mkEnv Controller { .. } = (env, map snd inps, map snd outs)
  where
  env = Env { envEnums   = Map.fromList [ (eName e, e) | e <- cEnums ]
            , envConstrs = Map.fromList constrs
            , envVars    = Map.fromList (inps ++ outs)
            , envVars'   = Map.fromList (map swap (inps ++ outs)) }

  swap (n,Slugs.VarBool v)    = (v,n)
  swap (n,Slugs.VarNum v _ _) = (v,n)

  constrs = concat [ zip eCons [0 .. ] | EnumDef { .. } <- cEnums ]

  inps = [ (svName sv, mkVar env sv) | sv <- cInputs  ]
  outs = [ (svName sv, mkVar env sv) | sv <- cOutputs ]

mkVar :: Env -> StateVar -> Slugs.Var
mkVar env StateVar { .. } =
  case svType of

    TEnum n ->
      let EnumDef { .. } = lookupEnum n env
       in Slugs.VarNum (mangleName svName) 0 (length eCons - 1)

    TInt ->
      case svBounds of
        Just (lo,hi) -> Slugs.VarNum (mangleName svName) lo hi
        Nothing      -> panic "mkDecl: Missing bounds for Int-typed state var"

    TBool ->
      Slugs.VarBool (mangleName svName)

    TFree{} -> panic "mkVar: Free variable"
    TFun{}  -> panic "mkVar: function-typed state variable"


lookupEnum :: Name -> Env -> EnumDef
lookupEnum n Env { .. } = Map.findWithDefault missing n envEnums
  where
  missing = panic ("lookupEnum: Enum missing from environment: " ++ show n)

lookupVar :: Name -> Env -> Slugs.Var
lookupVar n Env { .. } = Map.findWithDefault missing n envVars
  where
  missing = panic ("lookupVar: Var missing from environment: " ++ show n)

lookupConstr :: Name -> Env -> Int
lookupConstr n Env { .. } = Map.findWithDefault missing n envConstrs
  where
  missing = panic ("lookupConstr: Constr missing from environment: " ++ show n)

mangleName :: Name -> String
mangleName n = T.unpack (nameText n) ++ "_" ++ show (nameUnique n)
