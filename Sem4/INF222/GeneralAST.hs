data Term = TermRep String [Term] deriving (Show, Eq, Read)

tvar :: String -> Term
tvar vid = TermRep vid []

tun :: String -> Term -> Term
tun uop el = TermRep uop [el]

tbin :: String -> Term -> Term -> Term
tbin bop el e2 = TermRep bop [el, e2]

-- build term from scratch: a*b + c*d
ex1s = TermRep "+" 
       [TermRep "*"
            [TermRep "a" [], TermRep "b" []]
        ,TermRep "*"
            [TermRep "c" [], TermRep "d" []]
        ]

ex1t = tbin "+" (tbin "*" (tvar "a"))