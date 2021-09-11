module Assignment2 where
--Oppg 2.1

-- If-then-else
--
-- if -> expr -> then -> stmt -------------------> 
--         |                    |
--         |                    |
--         -->  else ->  stmt -->
--

-- Trinary operators:
-- _ -> ? -> _ -> : -> _

-- (expr) -> ? -> stmt ------------------>
--           |               |
--           |               |
--           --> : -> stmt -->

--Oppg 2.2

-- General extended BTL abstract syntax
import Text.Read
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

data Binop
    = Plus | Minus | Or | Mult | Slash | Div | Mod | And | Eq | Lt | Gt | Ne | Le | Ge
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
bad1s :: Expr
bad1s = Unary "-" (Unary "not" (Varid "x"))
bad1t = tun "-" (tun "not" (tvar "x"))

-- Typecheck
{-
--------------------------
-- | Infers the type of an expression
typecheck :: Declarations -> Expr -> Type 

{- |
typecheck decls@(ftypes,vtypes) (Unary expr1 expr2) =
    if Tint == typecheck decls expr
        then Tint 
        else error $ 
            "Unary operator Uminus receives wrongly typed argument " ++ (show expr) 
-}

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


main1 = do
    print $ typecheck declarations ex1s
    

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

main2 = do
    print $ typeinfer declarations ex1s 

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

-}

-- 2.3

-- 2.4

data JSONValue
    = JInteger Int
    | JString String
    | JBool Bool
    | JNull
    deriving (Eq, Read, Show)

type JNumber = (Int, Int, Int, Int)

-- 2.5
pp :: JSONValue -> String
pp = undefined 

ppi :: Int -> JSONValue -> String
ppi = undefined
--Datatypene til Ast
data Ast
  = Word String
  | Num Int
  | Mult Ast Ast
  | Plus Ast Ast
  | Minus Ast Ast
  deriving (Eq, Show)

collectWhile :: (Char -> Bool) -> String -> (String, String)
collectWhile x y = (takeWhile x y, dropWhile x y)

--Hjelpefunksjon som sjekker hva token elementet vi får inn er av
isNumToken, isWordToken :: String -> Bool
isNumToken xs = takeWhile isDigit xs == xs
isWordToken xs = takeWhile isAlpha xs == xs

--Tokenize, gjenbruk av kode fra ukesoppg. 5. Funksjon som sjekker hvilket tegn vi har fått som input, og plasserer den i rett katevalri
tokenize :: [Char] -> [String]
tokenize [] = []
tokenize ('+' : xs) = "+" : tokenize xs
tokenize ('*' : xs) = "*" : tokenize xs
tokenize (' ' : xs) = tokenize xs
tokenize ('-' : xs) = "-" : tokenize xs
tokenize (x : xs)
  | isDigit x =
    let (ys, y) = collectWhile isDigit xs --isDigit hentet fra Data.Char
     in (x : ys) : tokenize y
  | isAlpha x =
    let (ys, y) = collectWhile isAlpha xs --isAlpha hentet fra Data.Char
     in (x : ys) : tokenize y
  | otherwise = error ("unexpected character " ++ show x)

--parse funksjon som parser faktorer (int og string)
parseNumOrWord :: [String] -> (Ast, [String])
parseNumOrWord [] = error "unexpected end of input"
parseNumOrWord (x : xs)
  | isNumToken x = (Num (read x), xs)
  | isWordToken x = (Word x, xs)
  | otherwise = error ("unrecognized token " ++ show x)

--parse funksjon som parser multiplikasjon (Mult)
parseMult :: [String] -> (Ast, [String])
parseMult xs
  =  let (y1, xs1) = parseNumOrWord xs
     in  val y1 xs1
     
  where val o ("*" : xs2)
          = let (y2, xs3) = parseNumOrWord xs2
            in val (Mult o y2) xs3
        val o end = (o, end)

--parse funksjon som parser addisjon (Plus)
parsePlus :: [String] -> (Ast, [String])
parsePlus xs
  =  let (y1, xs1) = parseMult xs
     in  val y1 xs1

  where val o ("+" : xs2)
          = let (y2, xs3) = parseMult xs2
            in val (Plus o y2) xs3
        val o end = (o, end)

--parse funksjon som parser subtraksjon (Minus)
parseMinus :: [String] -> (Ast, [String])
parseMinus xs
  =  let (y1, xs1) = parsePlus xs
     in  val y1 xs1

  where val o ("-" : xs2)
          = let (y2, xs3) = parsePlus xs2
            in val (Minus o y2) xs3
        val o end = (o, end)

--Wrapper funksjon parse rundt parseMinus, som kaller på de andre funksjonene. Gir error dersom ulovlig
parse :: String -> Ast
parse x =

  case parseMinus (tokenize x) of
    (i, []) -> i
    (_, j : _) -> error ("unexpected token " ++ (show j))

--Oppg.2
vis :: Ast -> IO ()
vis ast = putStr (vis' ast)

indent :: Int -> [Char]
indent n = concat $ take n (repeat "   ")

vis' :: Ast -> String
vis' ast = vissH ast 0

vissH :: Ast -> Int -> String
vissH (Mult a a') n = indent n ++ "Mult"  ++ "\n" ++ vissH a (n+1) ++ vissH a' (n+1)
vissH (Plus a a' ) n = indent n ++ "Plus"   ++ "\n" ++ vissH a (n+1) ++ vissH a' (n+1)
vissH (Minus a a' ) n = indent n ++ "Minus"   ++ "\n" ++ vissH a (n+1) ++ vissH a' (n+1)
vissH (Num i    ) n = indent n ++ "Num " ++ show i ++ "\n"
vissH (Word i    ) n = indent n ++ "Word " ++ i ++ "\n"