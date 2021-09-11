-- inf222-2021-lec0501-ast
-- Magne Haveraaen, 2021-02-03

-- Fully typed extended BTL abstract syntax
{- |
Symbol uplus : iexpr → iexpr ;
Symbol uminus : iexpr → iexpr ;
Symbol unot : bexpr → bexpr ;
Symbol intLiteral : integer → iexpr ;
Symbol booLiteral : boolean → bexpr ;
Symbol ivarid : string → iexpr ;  Symbol bvarid : string → bexpr ;
-- Symbol functionCall : string × expr∗ → expr ;
Symbol ibinaryExpr : ibinop × iexpr × iexpr → iexpr ;
Symbol bbinaryExpr : bbinop × bexpr × bexpr → bexpr ;
Symbol ibbinaryExpr : ibbinop × iexpr × iexpr → bexpr ;
Symbol iifexpr : bexpr × iexpr × iexpr → iexpr ;
Symbol bifexpr : bexpr × bexpr × bexpr → bexpr ;

Symbol plus : → ibinop ;
Symbol or : → bbinop ;
Symbol le : → ibbinop ;
… 
-}
data IExpr
    = Uplus IExpr
    | Uminus IExpr
    | Intliteral Integer
    | IVarid String
    -- | FunctionCall String [Expr]
    | IBinaryExpr Ibinop IExpr IExpr
    | IIfexpr BExpr IExpr IExpr
  deriving (Show, Eq, Read)
data BExpr
    = Unot BExpr
    | BooLiteral Bool
    | BVarid String
    -- | FunctionCall String [Expr]
    | BBinaryExpr Bbinop BExpr BExpr
    | IBbinaryExpr IBbinop IExpr IExpr
    | BIfexpr BExpr BExpr BExpr
  deriving (Show, Eq, Read)

data Ibinop = Iplus | Iminus | Imult | Idiv | Imod deriving (Show, Eq, Read)
data Bbinop = Bor | Band deriving (Show, Eq, Read)
data IBbinop = IBeq | IBlt | IBne | IBle | IBge deriving (Show, Eq, Read)


-- build term for: a*b + c*d
ex1 = 
    IBinaryExpr Iplus 
        (IBinaryExpr Imult (IVarid "a") (IVarid "b")) 
        (IBinaryExpr Imult (IVarid "c") (IVarid "d"))

-- build term for: (a*b + c) * d
ex2 =
    IBinaryExpr Imult 
        (IBinaryExpr Iplus 
            (IBinaryExpr Imult (IVarid "a") (IVarid "b")) 
            (IVarid "c")) 
        (IVarid "d")


-- can not represent bad term: -(not(x))
-- bad1b = Uminus (Unot (BVarid "x"))
-- bad1i = Uminus (Unot (IVarid "x"))
