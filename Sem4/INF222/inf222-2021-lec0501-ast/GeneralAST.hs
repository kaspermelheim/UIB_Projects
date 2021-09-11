-- inf222-2021-lec0501-ast
-- Magne Haveraaen, 2021-02-03

-- General abstract syntax
{- |
 Symbol termRep : string × term* → term ;
-}
data Term = TermRep String [Term]
  deriving (Show, Eq, Read)


-- Create a term for a variable
tvar :: String -> Term
tvar vid = TermRep vid []
-- Create a term for a unary operation call
tun :: String -> Term -> Term
tun uop e1 = TermRep uop [e1]
-- Create a term for a binary operation call
tbin :: String -> Term -> Term -> Term
tbin bop e1 e2 = TermRep bop [e1, e2]

-- build term from scratch: a*b + c*d
ex1s =
    TermRep "+" 
    [TermRep "*" 
        [TermRep "a" [],TermRep "b" []]
    ,TermRep "*" 
        [TermRep "c" [],TermRep "d" []]
    ]
-- build term from support tools
ex1t = tbin "+" (tbin "*" (tvar "a") (tvar "b")) (tbin "*" (tvar "c") (tvar "d"))

-- build term from scratch: (a*b + c) * d
ex2s =
    TermRep "*" 
    [TermRep "+" 
        [TermRep "*" 
            [TermRep "a" [],TermRep "b" []]
        ,TermRep "c" []]
    ,TermRep "d" []]

-- build term from support tools
ex2t = tbin "*" (tbin "+"  (tbin "*" (tvar "a") (tvar "b")) (tvar "c")) (tvar "d")



-- build bad term: -(not(x))
bad1s = TermRep "-" [TermRep "not" [TermRep "x" []] ]
bad1t = tun "-" (tun "not" (tvar "x"))
