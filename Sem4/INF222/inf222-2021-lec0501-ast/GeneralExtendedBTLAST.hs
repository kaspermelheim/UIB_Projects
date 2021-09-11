-- inf222-2021-lec0501-ast
-- Magne Haveraaen, 2021-02-03

-- General extended BTL abstract syntax
{- |
Symbol unary : string × expr → expr ;
Symbol intLiteral : integer → expr ;
Symbol booLiteral : boolean → expr ;
Symbol varid : string → expr ;
Symbol functionCall : string × expr* → expr ;
Symbol binaryExpr : string × expr × expr → expr ;
Symbol ifexpr : expr × expr × expr → expr ;
-}
data Expr
    = Unary String Expr
    | Intliteral Integer
    | BooLiteral Bool
    | Varid String
    | FunctionCall String [Expr]
    | BinaryExpr String Expr Expr
    | Ifexpr Expr Expr Expr
  deriving (Show, Eq, Read)


-- Create a term for a variable
tvar :: String -> Expr
tvar vid = Varid vid
-- Create a term for a unary operation call
tun :: String -> Expr -> Expr
tun uop e1 = Unary uop e1
-- Create a term for a binary operation call
tbin :: String -> Expr -> Expr -> Expr
tbin bop e1 e2 = BinaryExpr bop e1 e2

-- build term from scratch: a*b + c*d
ex1s = 
    BinaryExpr "+" 
    (BinaryExpr "*" (Varid "a") (Varid "b")) 
    (BinaryExpr "*" (Varid "c") (Varid "d"))
-- build term from support tools
ex1t = tbin "+" (tbin "*" (tvar "a") (tvar "b")) (tbin "*" (tvar "c") (tvar "d"))

-- build term from scratch: (a*b + c) * d
ex2s =
    BinaryExpr "*" 
        (BinaryExpr "+" 
            (BinaryExpr "*" (Varid "a") (Varid "b")) 
            (Varid "c")) 
        (Varid "d")
-- build term from support tools
ex2t = tbin "*" (tbin "+"  (tbin "*" (tvar "a") (tvar "b")) (tvar "c")) (tvar "d")



-- build bad term: -(not(x))
bad1s = Unary "-" (Unary "not" (Varid "x"))
bad1t = tun "-" (tun "not" (tvar "x"))
