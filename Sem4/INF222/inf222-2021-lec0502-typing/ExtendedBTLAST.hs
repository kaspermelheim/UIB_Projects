-- inf222-2021-lec0502-typing
-- Magne Haveraaen, 2021-02-03
-- Extended from inf222-2021-lec0501-ast/GeneralExtendedBTLAST.hs

module ExtendedBTLAST where

-- | Extended BTL abstract syntax
{- |
Symbol uplus : expr → expr ;
Symbol uminus : expr → expr ;
Symbol unot : expr → expr ;
Symbol intLiteral : integer → expr ;
Symbol booLiteral : boolean → expr ;
Symbol varid : string → expr ;
Symbol functionCall : string × expr∗ → expr ;
Symbol binaryExpr : binop × expr × expr → expr ;
Symbol ifexpr : expr × expr × expr → expr ;

Symbol plus : → binop ;
Symbol minus : → binop ;
Symbol or : → binop ;
Symbol mult : → binop ;
…
Symbol le : → binop ;
Symbol ge : → binop ;
-}
data Expr
    = Uplus Expr
    | Uminus Expr
    | Unot Expr
    | Intliteral Integer
    | BooLiteral Bool
    | Varid String
    | FunctionCall String [Expr]
    | BinaryExpr Binop Expr Expr
    | Ifexpr Expr Expr Expr
  deriving (Show, Eq, Read)
data Binop
    = Plus | Minus | Or | Mult | Slash | Div | Mod | And | Eq | Lt | Gt | Ne | Le | Ge
  deriving (Show, Eq, Read)

--------------------------
-- | Functions for building expression terms

-- Create a term for a variable
tvar :: String -> Expr
tvar vid = Varid vid
-- Create a term for an integer literal
tint :: Integer -> Expr
tint lit = Intliteral lit
-- Create a term for a bool literal
tboo :: Bool -> Expr
tboo lit = BooLiteral lit
-- Create a term for a unary operation call
tup :: Expr -> Expr
tup e1 = Uplus e1
tum :: Expr -> Expr
tum e1 = Uminus e1
tun :: Expr -> Expr
tun e1 = Unot e1
-- Create a term for a binary operation call
tbin :: Binop -> Expr -> Expr -> Expr
tbin bop e1 e2 = BinaryExpr bop e1 e2
-- Create a term for an if expression
tife :: Expr -> Expr -> Expr -> Expr
tife cond e1 e2 = Ifexpr cond e1 e2
-- Create a term for a general function call
tfun :: String -> [Expr] -> Expr
tfun fname args = FunctionCall fname args


--------------------------
-- | Some example terms

-- build term for: a*b + c*d
ex1 :: Expr
ex1 = tbin Plus (tbin Mult (tvar "a") (tvar "b")) (tbin Mult (tvar "c") (tvar "d"))

-- build term for: (a*b + c) * d
ex2 :: Expr
ex2 = tbin Mult (tbin Plus  (tbin Mult (tvar "a") (tvar "b")) (tvar "c")) (tvar "d")

-- build term for: if (a*b ≤ c) then a else c
ex3 :: Expr
ex3 = tife (tbin Le (tbin Mult (tvar "a") (tvar "b")) (tvar "c")) (tvar "a") (tvar "c")

-- build term for function call: func1 (ex3, ex2)
ex4 :: Expr
ex4 = tfun "func1" [ex3, ex2]

-- build term for function call: func2 (24, 25, 14 ≤ 61)
ex5 :: Expr
ex5 = tfun "func2" [tint 24, tint 25, tbin Le (tint 14) (tint 61)]


-- build bad term: -(not(x))
bad1 :: Expr
bad1 = tum (tun (tvar "x"))
