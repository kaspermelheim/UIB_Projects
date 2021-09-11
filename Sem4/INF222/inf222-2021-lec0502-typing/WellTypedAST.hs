-- | Analysis functions for extended BTL ASTs.
--
-- Author: Magne Haveraaen
-- Since: 2021-02-04

module WellTypedAST where

import ExtendedBTLAST
import ExtendedBTLDeclarations

--------------------------
-- | Infers the type of an expression
typecheck :: Declarations -> Expr -> Type 
typecheck decls@(ftypes,vtypes) (Uplus expr) =
    if Tint == typecheck decls expr
        then Tint 
        else error $ 
            "Unary operator Uplus receives wrongly typed argument " ++ (show expr)
typecheck decls@(ftypes,vtypes) (Uminus expr) =
    if Tint == typecheck decls expr
        then Tint 
        else error $ 
            "Unary operator Uminus receives wrongly typed argument " ++ (show expr)
typecheck decls@(ftypes,vtypes) (Unot expr) =
    if Tbool == typecheck decls expr
        then Tbool 
        else error $ 
            "Unary operator Unot receives wrongly typed argument " ++ (show expr)
typecheck decls (Intliteral num) = Tint
typecheck decls (BooLiteral num) = Tbool
typecheck decls@(ftypes,vtypes) (Varid str) = findvartype str vtypes
typecheck decls@(ftypes,vtypes) (FunctionCall str exprs) =
    if findargtypes str ftypes == [typecheck decls expr | expr <- exprs] 
        then findrestype str ftypes 
        else error $ "Function \"" ++ str ++ "\" receives wrongly typed arguments " ++ (show exprs)
typecheck decls@(ftypes,vtypes) (BinaryExpr bin expr1 expr2) =
    if elem bin [Plus, Minus, Mult, Div, Mod ] then checkbin bin Tint Tint (expr1, expr2) decls
    else if elem bin [Or, And] then checkbin bin Tbool Tbool (expr1, expr2) decls
    else if elem bin [Eq, Lt, Gt, Ne, Le, Ge] then checkbin bin Tint Tbool (expr1, expr2) decls
    else error $ 
            "Unhandled bunary operations " ++ (show bin) 
            ++ " for arguments " ++ (show (expr1,expr2))
typecheck decls@(ftypes,vtypes) ifexpr@(Ifexpr cond e1 e2) =
    if Tbool == typecheck decls cond && typecheck decls e1 == typecheck decls e2
        then typecheck decls e1
        else error $ "If-expression has wrong arguments " ++ (show ifexpr)

-- | Check the arguments to the binary int/bool/comparison operator
checkbin :: Binop -> Type -> Type -> (Expr, Expr) -> Declarations -> Type
checkbin bin texpa texpr (expr1, expr2) decls =
    if (texpa, texpa) == (typecheck decls expr1, typecheck decls expr2)
        then texpr 
        else error $ 
            "Binary operator \"" ++ (show bin)
            ++ "\" receives wrongly typed arguments " ++ (show (expr1,expr2))


main = do
    print $ typecheck declarations ex1 
    print $ typecheck declarations ex2
    print $ typecheck declarations ex3 
    print $ typecheck declarations ex4 
    print $ typecheck declarations ex5 
    print $ typecheck declarations bad1 

