{-# LANGUAGE RecordWildCards #-}

module Scope.Name (
    Name(), nameText, nameOrigin,
    Origin(..),
    Supply(), emptySupply, nextUnique,
    mkName,
  ) where

import           Data.Function (on)
import qualified Data.Text.Lazy as L
import           Text.Location (Range)


-- Names -----------------------------------------------------------------------

data Origin = FromController !(Range FilePath)
              -- ^ Top-level controller, and its region

            | FromDecl !(Range FilePath) !Name
              -- ^ Top-level definition region and parent controller

            | FromParam !(Range FilePath) !Name
              -- ^ Parameter definition region and parent function

              deriving (Show)


data Name = Name { nText   :: !L.Text
                 , nUnique :: !Int
                 , nOrigin :: !Origin
                 } deriving (Show)

instance Eq Name where
  (==) = (==) `on` nUnique
  (/=) = (/=) `on` nUnique
  {-# INLINE (==) #-}
  {-# INLINE (/=) #-}

instance Ord Name where
  compare = compare `on` nUnique
  {-# INLINE compare #-}

nameOrigin :: Name -> Origin
nameOrigin  = nOrigin

nameText :: Name -> L.Text
nameText  = nText


-- Name Supply -----------------------------------------------------------------

newtype Supply = Supply Int

emptySupply :: Supply
emptySupply  = Supply 0

nextUnique :: Supply -> (Int,Supply)
nextUnique (Supply n) =
  let n' = n + 1
   in n `seq` (n, Supply n')


-- Name Construction -----------------------------------------------------------

mkName :: Origin -> L.Text -> Supply -> (Name,Supply)
mkName nOrigin nText s =
  let (nUnique,s') = nextUnique s
   in (Name { .. }, s')