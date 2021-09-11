-- | Type inference functions for extended BTL ASTs.
-- | This is a translation from the regular AST to an AST decorated with types. 
--
-- Author: Magne Haveraaen
-- Since: 2021-02-04

module TypeinferenceBTL where

import ExtendedBTLAST
import ExtendedBTLDeclarations

--------------------------
-- | Types in extended BTL ASTs augmented for type errors
data EType = ETint | ETbool | Error deriving (Show, Eq, Read)
-- | Convert from old types to error type.
typetoetype :: Type -> EType
typetoetype Tint = ETint
typetoetype Tbool = ETbool

-- | Type extended AST
data TExpr
    = TUplus TExpr EType
    | TUminus TExpr EType
    | TUnot TExpr EType
    | TIntliteral Integer
    | TBooLiteral Bool
    | TVarid String EType
    | TFunctionCall String [TExpr] EType
    | TBinaryExpr Binop TExpr TExpr EType
    | TIfexpr TExpr TExpr TExpr EType
  deriving (Show, Eq, Read)

--------------------------
-- | Gives the type of a TExpression (no recursion)
typeof :: TExpr -> EType
typeof (TUplus te et) = et
typeof (TUminus te et) = et
typeof (TUnot te et) = et
typeof (TIntliteral num) = ETint
typeof (TBooLiteral bool) = ETbool
typeof (TVarid str et) = et
typeof (TFunctionCall str tes et) = et
typeof (TBinaryExpr binop te1 te2 et) = et
typeof (TIfexpr cont te1 te2 et) = et

-- | Find type of a variable
tfindvartype :: String -> [Vartype] -> EType
tfindvartype name ((vname,vtype):vars) =
    if name == vname then typetoetype vtype else tfindvartype name vars
tfindvartype name [] = Error
-- | Find function declaration
tfindfun :: String -> [Funtype] -> ([EType],EType)
tfindfun name ((fname,fpars,fret):funs) =
    if name == fname 
    then ([typetoetype fpar | fpar <- fpars],typetoetype fret) 
    else tfindfun name funs
tfindfun name [] = ([],Error)

--------------------------
-- | Creates a typed expression AST from a normal expression AST.
typeinfer :: Declarations -> Expr -> TExpr 
typeinfer decls@(ftypes,vtypes) (Uplus expr) = TUplus texpr tret 
    where 
        texpr = typeinfer decls expr
        tret = if typeof texpr == ETint then ETint else Error
typeinfer decls@(ftypes,vtypes) (Uminus expr) = TUminus texpr tret 
    where 
        texpr = typeinfer decls expr
        tret = if typeof texpr == ETint then ETint else Error
typeinfer decls@(ftypes,vtypes) (Unot expr) = TUnot texpr tret 
    where 
        texpr = typeinfer decls expr
        tret = if typeof texpr == ETbool then ETbool else Error
typeinfer decls (Intliteral num) = TIntliteral num
typeinfer decls (BooLiteral bool) = TBooLiteral bool
typeinfer decls@(ftypes,vtypes) (Varid str) = TVarid str (tfindvartype str vtypes)
typeinfer decls@(ftypes,vtypes) (FunctionCall str exprs) = TFunctionCall str texprs tret'
    where 
        (tpars,tret) = tfindfun str ftypes
        texprs = [ typeinfer decls expr | expr <- exprs ]
        targs = [ typeof texpr | texpr <- texprs ]
        tret' = if tpars == targs then tret else Error
typeinfer decls@(ftypes,vtypes) (BinaryExpr bin expr1 expr2) =
    TBinaryExpr bin texpr1 texpr2 tret
    where
        texpr1 = typeinfer decls expr1
        texpr2 = typeinfer decls expr2
        tret =  if elem bin [Plus, Minus, Mult, Div, Mod ] 
                  && typeof texpr1 == ETint && typeof texpr2 == ETint 
                then ETint
                else if elem bin [Or, And] 
                  && typeof texpr1 == ETbool && typeof texpr2 == ETbool 
                then ETbool
                else if elem bin [Eq, Lt, Gt, Ne, Le, Ge] 
                  && typeof texpr1 == ETint && typeof texpr2 == ETint 
                then ETbool
                else Error
typeinfer decls@(ftypes,vtypes) (Ifexpr cond e1 e2) = TIfexpr tcond te1 te2 tret
    where
        tcond = typeinfer decls cond
        te1 = typeinfer decls e1
        te2 = typeinfer decls e2
        tret =  if typeof tcond == ETbool && typeof te1 == typeof te2
                then typeof te1
                else Error

main = do
    print $ typeinfer declarations ex1 
    print $ typeinfer declarations ex2
    print $ typeinfer declarations ex3 
    print $ typeinfer declarations ex4 
    print $ typeinfer declarations ex5 
    print $ typeinfer declarations bad1 

