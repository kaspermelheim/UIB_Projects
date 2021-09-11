module Heartbleed where

import State ( extract, insert, getTop, subLocation, MemorySize, Store )
import Data.Word (Word8)

-- | Let an external user check the responsiveness of the service.
-- Insert the input packet (of words) into store and return the requested number of words.
heartbeat :: [Word8] -> MemorySize -> Store -> (Store,[Word8])
heartbeat inp size store = ( store', extract loc' size store')
                            where
                                loc' = subLocation ( getTop store ) (fromIntegral ( length inp ))
                                store' = insert loc' inp store
                            
covidDatabase = undefined