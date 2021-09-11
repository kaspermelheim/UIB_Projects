-- | Analysis functions for extended BTL ASTs.
--
-- Author: Magne Haveraaen
-- Since: 2021-02-04

module WellTypedAST where

import ExtendedBTLAST
import ExtendedBTLDeclarations

--------------------------
-- | Infers the type of an expression
-- |
-- | NOTE: See TypeInferenceBTL.hs for a more heavily commented version which
-- | works similarly -- their type-checking logic is exactly the same. The
-- | difference is the result (this function returns a single type, while
-- | typeInfer returns the whole AST with types added to all expressions), and
-- | how they handle type-errors (this function raises an exception (error)
-- | with a detailed description of why typechecking failed, while typeInfer
-- | only tags the expression with the type `Error` to signal that _something_
-- | went wrong.
typeCheck :: Declarations -> Expr -> Type
typeCheck decls@(ftypes,vtypes) (UPlus expr) =
    if TInt == typeCheck decls expr
        then TInt
        else error $
            "Unary operator UPlus receives wrongly typed argument " ++ (show expr)
typeCheck decls@(ftypes,vtypes) (UMinus expr) =
    if TInt == typeCheck decls expr
        then TInt
        else error $
            "Unary operator UMinus receives wrongly typed argument " ++ (show expr)
typeCheck decls@(ftypes,vtypes) (UNot expr) =
    if TBool == typeCheck decls expr
        then TBool
        else error $
            "Unary operator UNot receives wrongly typed argument " ++ (show expr)
typeCheck decls (IntLiteral num) = TInt
typeCheck decls (BoolLiteral num) = TBool
typeCheck decls@(ftypes,vtypes) (VarId str) = findVarType str vtypes
typeCheck decls@(ftypes,vtypes) (FunctionCall str exprs) =
    if findArgTypes str ftypes == [typeCheck decls expr | expr <- exprs]
        then findResultType str ftypes
        else error $ "Function \"" ++ str ++ "\" receives wrongly typed arguments " ++ (show exprs)
typeCheck decls@(ftypes,vtypes) (BinaryExpr bin expr1 expr2) =
    if elem bin [Plus, Minus, Mult, Div, Mod ] then checkbin bin TInt TInt (expr1, expr2) decls
    else if elem bin [Or, And] then checkbin bin TBool TBool (expr1, expr2) decls
    else if elem bin [Eq, Lt, Gt, Ne, Le, Ge] then checkbin bin TInt TBool (expr1, expr2) decls
    else error $
            "Unhandled binary operations " ++ (show bin)
            ++ " for arguments " ++ (show (expr1,expr2))
typeCheck decls@(ftypes,vtypes) ifexpr@(IfExpr cond e1 e2) =
    if TBool == typeCheck decls cond && typeCheck decls e1 == typeCheck decls e2
        then typeCheck decls e1
        else error $ "If-expression has wrong arguments " ++ (show ifexpr)

-- | Check the arguments to the binary int/bool/comparison operator
checkbin :: Binop -> Type -> Type -> (Expr, Expr) -> Declarations -> Type
checkbin bin texpa texpr (expr1, expr2) decls =
    if (texpa, texpa) == (typeCheck decls expr1, typeCheck decls expr2)
        then texpr
        else error $
            "Binary operator \"" ++ (show bin)
            ++ "\" receives wrongly typed arguments " ++ (show (expr1,expr2))


testTypeCheck = do
    print $ typeCheck declarations ex1
    print $ typeCheck declarations ex2
    print $ typeCheck declarations ex3
    print $ typeCheck declarations ex4
    print $ typeCheck declarations ex5
    print $ typeCheck declarations bad1

