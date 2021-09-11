-- | Operation and function declarations for extended BTL ASTs.
--
-- Author: Magne Haveraaen
-- Since: 2021-02-04

module ExtendedBTLDeclarations where

import ExtendedBTLAST


--------------------------
-- | Types in extended BTL ASTs.
data Type = Tint | Tbool deriving (Show, Eq, Read)
-- | Function types
type Funtype = (String, [Type],Type)
-- | Find argument types and result type, repsectively
findargtypes :: String -> [Funtype] -> [Type]
findargtypes name ((fname,targs,tres):funs) =
    if name == fname then targs else findargtypes name funs
findargtypes name [] = error $ "Unknown function name " ++ name
findrestype :: String -> [Funtype] -> Type
findrestype name ((fname,targs,tres):funs) =
    if name == fname then tres else findrestype name funs
findrestype name [] = error $ "Unknown function name " ++ name

-- | Variable types
type Vartype = (String,Type)
vartype :: [String] -> Type -> [Vartype]
vartype vnames tname = [ (vname,tname) | vname <- vnames]
-- | Find type of a variable
findvartype :: String -> [Vartype] -> Type
findvartype name ((vname,vtype):vars) =
    if name == vname then vtype else findvartype name vars
findvartype name [] = error $ "Unknown variable name " ++ name

-- | Collated declarations
type Declarations = ([Funtype],[Vartype])

--------------------------
-- | Declared functions
func1::Funtype 
func1 = ("func1",[Tint, Tint],Tint)
func2::Funtype 
func2 = ("func2",[Tint, Tint, Tbool],Tint)

-- | All declarations
declarations :: Declarations
declarations = 
    ([func1,func2],
     varints++varboos
    )


--------------------------
-- variables
varints = vartype ["a","b","c","d"] Tint
varboos = vartype ["x"] Tbool
