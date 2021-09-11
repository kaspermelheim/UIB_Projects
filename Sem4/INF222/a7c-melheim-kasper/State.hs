module State where

-- Import unsigned integers (Modulus integers)
import Data.Word (Word8, Word16)
-- Import array datatypes
import Data.Array
import Data.Binary (Binary, encode, decode)
import Data.ByteString.Lazy (pack, unpack)
import qualified Data.Set as S

-- Store
type Store = (S.Set Location, Array Location Word8)

type Location = Word16
type MemorySize = Word16

-- | Zero initialised store of a given size
newStore :: MemorySize -> Store
newStore memSize = (S.fromList [(memSize-2),(memSize-1)] ,array (0,memSize-1) ([(i,0) | i <- [0..(memSize-2)]] ++ [(memSize-1, fromIntegral memSize-1)]))

--Test store
a :: Store
a = newStore 8

-- | Copies the contents of a data structure within the store,
-- copies MemorySize words from source location to target location.
copy :: Location -> MemorySize -> Location -> Store -> Store
copy loc1 memSize loc2 store = insert loc1 (extract loc2 memSize store) store

-- | Get the top of the stack (lowest address in use)
getTop :: Store -> Location
getTop (_, store) = fromWords (map (store !) [(snd (bounds store)-1)..(snd (bounds store))])

-- | Set the top of the stack (lowest address in use)
setTop :: Location -> Store -> Store
setTop loc (list, store) = insert (snd (bounds store) - 1) (toWords loc) (list, store)

-- | Copies the list of words into the target location onwards,
-- overwriting existing data
insert :: Location -> [Word8] -> Store -> Store
insert loc elem (list, store) = (foldr (S.insert) list [loc..loc + (fromIntegral (length elem) - 1)],store // zip [loc..(loc + fromIntegral (length elem - 1))] elem)

-- | Copies memory size numbers of words from source location to the list.
extract :: Location -> MemorySize -> Store -> [Word8]
extract loc memSize (_, store) = map (store !) [loc..loc + (memSize - 1)] 

firstFit :: MemorySize -> Store -> Location
firstFit memSize (list, store) = firstLoop memSize (list, store) 0

firstLoop :: MemorySize -> Store -> Location -> Location
firstLoop memSize (list, store) loc = if loc > (snd (bounds store)) then error "Error, out of bounds."
                                      else if any (`S.member` list) [loc..loc + (memSize - 1)] then firstLoop memSize (list, store) loc+1
                                      else loc



-- | Arithmetic on memory size and locations
addSize :: MemorySize -> MemorySize -> MemorySize
addSize = (+)

subSize :: MemorySize -> MemorySize -> MemorySize
subSize = (-)

multSize :: Integer -> MemorySize -> MemorySize
multSize = (*) . fromIntegral

addLocation :: Location -> MemorySize -> Location
addLocation = (+)

subLocation :: Location -> MemorySize -> Location
subLocation = (-)


--Hjelpefunksjoner
toWords :: Binary a => a -> [Word8]
toWords = unpack . encode

fromWords :: Binary a => [Word8] -> a
fromWords = decode . pack

{--
-- | Concatenation property of store model
concatInStoreAxiom str1 str2 loc store = assert ( str1 ++str2 == extract loc size store'') "Success "
                                            where
                                              size = length str1 + length str2
                                              loc2 = addLocation loc ( length str1 )
                                              store' = insert loc str1 store
                                              store'' = insert loc2 str2 store'

--}