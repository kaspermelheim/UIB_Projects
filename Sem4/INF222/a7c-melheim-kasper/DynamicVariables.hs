module DynamicVariables where

import State 
import TypeExpression

type Variable = (String, Location, MemorySize, Type)
type Environment = ([Variable], Store)

--Test
b :: Environment
b = newEnvironment 24

--Create new environment
newEnvironment :: MemorySize -> Environment
newEnvironment memSize = ([], newStore memSize)

--New
new :: String -> TypeExpression -> Environment -> Environment
new str typ (vars, store) = let memSize = sizeof typ
                                loc = firstFit memSize store 
                                typ' = getType typ
                            in ((str, loc, memSize, typ') : vars, insert loc (write typ) store)
                            
--Create new pointer
newPointer :: TypeExpression -> Environment -> (Location, Environment)
newPointer typ (vars, store) = let memSize = sizeof typ
                                   loc = firstFit memSize store 
                               in (loc, (vars, insert loc (write typ) store))