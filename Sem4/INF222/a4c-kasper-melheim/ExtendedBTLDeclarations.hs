-- | Operation and function declarations for extended BTL ASTs.
--
-- Author: Magne Haveraaen
-- Since: 2021-02-04

module ExtendedBTLDeclarations where

import ExtendedBTLAST

--------------------------
-- | Types in extended BTL ASTs.
data Type = TInt | TBool deriving (Show, Eq, Read)

-- | Function types
type FunType = (String, ([Type], Type))
-- | Find argument types for declared function
findArgTypes :: String -> [FunType] -> [Type]
findArgTypes name funs = case lookup name funs of
                           Just (argTypes, returnType) -> argTypes
                           Nothing -> error $ "Unknown function name " ++ name
-- | Find result type for declared function
findResultType :: String -> [FunType] -> Type
findResultType name funs = case lookup name funs of
                             Just (argTypes, returnType) -> returnType
                             Nothing -> error $ "Unknown function name " ++ name
-- | Alternative algorithm for finding argument types for declared function
findArgTypes' :: String -> [FunType] -> [Type]
findArgTypes' name ((fname,(argTypes,resType)):funs) =
    if name == fname then argTypes else findArgTypes' name funs
findArgTypes' name [] = error $ "Unknown function name " ++ name
-- | Alternative algorithm for finding result type for declared function
findResultType' :: String -> [FunType] -> Type
findResultType' name ((fname,(argTypes,resType)):funs) =
    if name == fname then resType else findResultType' name funs
findResultType' name [] = error $ "Unknown function name " ++ name

-- | Variable types
type VarType = (String, Type)
-- Find the type of a declared variable.
findVarType :: String -> [VarType] -> Type
findVarType name vars = case lookup name vars of
                          Just varType -> varType
                          Nothing -> error $ "Unknown variable name " ++ name

-- | Collated declarations
type Declarations = ([FunType], [VarType])
-- Components are accessed by pattern matching or fst/snd tuple projections.

--------------------------
-- | Declared functions

-- func1 takes 2 parameters (both of type Int) and has return type Int.
func1 :: FunType 
func1 = ("func1", ([TInt, TInt], TInt))

-- func1 takes 2 parameters (both of type Int) and has return type Int.
func2 :: FunType 
func2 = ("func2", ([TInt, TInt, TBool], TInt))

funcs = [func1, func2]

-- | All declarations
declarations :: Declarations
declarations = (funcs, vars)

--------------------------
-- variables
varType :: [String] -> Type -> [VarType]
varType vnames tname = [ (vname,tname) | vname <- vnames]

varInts = varType ["a","b","c","d"] TInt
varBools = varType ["x"] TBool

vars = varInts ++ varBools
