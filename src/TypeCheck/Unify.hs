{-# LANGUAGE RecordWildCards #-}
{-# LANGUAGE FlexibleContexts #-}

module TypeCheck.Unify (
    Env(), emptyEnv,
    UnifyError(..),
    Types(),
    unify,
    zonk
  ) where

import TypeCheck.AST

import qualified Data.IntMap.Strict as IntMap
import qualified Data.Map.Strict as Map
import qualified Data.Set as Set
import           MonadLib


-- External Interface ----------------------------------------------------------

-- | Unify these two types, and update the environment.
unify :: Types ty => ty -> ty -> Env -> Either UnifyError Env
unify a b = runUnify_ (unify' a b)

-- | Remove type variables from this type.
zonk :: Types ty => ty -> Env -> Either UnifyError ty
zonk a env =
  case runUnify (zonk' a) env of
    Right (a',_) -> Right a'
    Left err     -> Left err

data UnifyError = UnifyError Type Type
                  -- ^ Unification failed -- these two types don't unify.

                | OccursCheckFailure
                  -- ^ The occurs check failed during zonking.
                  deriving (Show)


-- Environment -----------------------------------------------------------------

data Env = Env { envCanon :: !(Map.Map TVar Int)
                 -- ^ Canonical names for type variables

               , envVars :: !(IntMap.IntMap Type)
                 -- ^ Values of type variables

               , envNext :: !Int
                 -- ^ The next canonical name to use
               } deriving (Show)


emptyEnv :: Env
emptyEnv  = Env { envCanon = Map.empty
                , envVars  = IntMap.empty
                , envNext  = 0
                }


-- Unification -----------------------------------------------------------------

type Unify = StateT Env (ExceptionT UnifyError Lift)

-- | Run a 'Unify' action.
runUnify :: Unify a -> Env -> Either UnifyError (a,Env)
runUnify m env = runLift (runExceptionT (runStateT env m))

-- | Run a 'Unify' action, and throw away its result.
runUnify_ :: Unify a -> Env -> Either UnifyError Env
runUnify_ m env =
  case runUnify m env of
    Right (_,env') -> Right env'
    Left  err      -> Left err

-- | Yield the next canonical name.
nextIx :: Unify Int
nextIx  =
  do Env { .. } <- get
     set $! Env { envNext = envNext + 1, .. }
     return envNext

-- | Bind a variable.
bindVar :: TVar -> Type -> Unify ()
bindVar var ty =
  do Env { .. } <- get
     case Map.lookup var envCanon of
       Just ix ->
         case IntMap.lookup ix envVars of
           Just ty' -> unify' ty' ty
           Nothing  -> set $! Env { envVars = IntMap.insert ix ty envVars, .. }

       Nothing ->
         do ix <- nextIx
            env <- get
            set $! env { envVars  = IntMap.insert ix ty envVars
                       , envCanon = Map.insert var ix envCanon }


class Types ty where
  -- | Unify two types, effecting the environment.
  unify' :: ty -> ty -> Unify ()

  -- | Remove type variables by looking them up in the environment.
  zonk' :: ty -> Unify ty


instance Types Type where
  unify' (TFree x) y = bindVar x y
  unify' y (TFree x) = bindVar x y

  unify' (TFun x1 y1) (TFun x2 y2) =
    do unify' x1 x2
       unify' y1 y2

  unify' TBool TBool = return ()
  unify' TNum  TNum  = return ()

  unify' (TEnum x) (TEnum y) | x == y = return ()

  unify' x y = raise (UnifyError x y)

  zonk'  = go Set.empty
    where

    go seen ty@(TFree x) =
      do Env { .. } <- get
         case Map.lookup x envCanon of
           Just ix ->
             case IntMap.lookup ix envVars of
               Just ty' | ix `Set.member` seen -> raise OccursCheckFailure
                        | otherwise            -> go (Set.insert ix seen) ty'

               Nothing -> return ty
           Nothing -> return ty

    go seen (TFun a b) =
      do a' <- go seen a
         b' <- go seen b
         return (TFun a' b')

    go _ ty = return ty
