module CustomTypes where

type MyString = [Char]

type PhoneNumber = String


data IntWrapper = WrapInt Int
    deriving Show

inc :: IntWrapper -> IntWrapper
inc (WrapInt x) = WrapInt (x + 1)

data Tuple = MkTuple Int Int deriving (Show)

swap :: Tuple -> Tuple
swap (MkTuple x y) = (MkTuple y x)

data Shape = Circle Float
            | Rectangle Float Float deriving (Show)

area :: Shape -> Float
area (Circle radius) = pi * radius ^ 2
area (Rectangle h w) = h * w 

data MyBool = MyFalse | MyTrue
    deriving (Show)

data MaybeFloat = MyNothing | MyJust Float deriving (Show)

maybeSquareRoot :: Float -> MaybeFloat
maybeSquareRoot x = if x < 0 then MyNothing else MyJust (sqrt x)

maybeSquareRoot' :: Float -> Maybe Float
maybeSquareRoot' x 
    | x < 0 = Nothing 
    | otherwise = Just (sqrt x)

data Result a b = Err a | Ok b deriving (Show)

data MyError = A | B | C

resultSquareRoot :: Float -> Result MyError Float
resultSquareRoot x 
    | x < 0 = Err C
    | otherwise = Ok (sqrt x)

data IntExpr
    = Number Int
    | Add IntExpr IntExpr
    | Mul IntExpr IntExpr
    | Negate IntExpr
    deriving (Show)

eval :: IntExpr -> Int
eval (Number i) = i
eval (Add e1 e2) = eval e1 + eval e1
eval (Mul e1 e2) = eval e1 * eval e2
eval (Negate e) = - (eval e)

-- BTL (Basic (Types and Programming Languages) Language)

data BTL
    = Zero
    | Succ BTL
    | Pred BTL
    | ETrue
    | EFalse
    | IsZero BTL

data Value = VBool Bool | VInt Int | VError String deriving (Show)

eval' :: BTL -> Int
eval' Zero = 0
eval' (Succ e) = case eval' e of
    VInt i -> VInt (i + 1)
    _ -> VError "Successor of non-int"
eval' (Pred e) = case eval' e of
    VInt i -> VInt (i + 1)
    _ -> VError "Predecessor of non-int"
eval (IsZero e) = case eval e of
    VInt 0 -> VBool True 
    VInt _ -> VBool False 
    _ -> VError "IsZero on non-int"
eval ETrue = VBool True 
eval EFalse = VBool False