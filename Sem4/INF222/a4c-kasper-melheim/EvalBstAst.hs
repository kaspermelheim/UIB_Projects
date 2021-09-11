-- | inf222-2021-lec0602-interpretation
-- | Evaluation function with environment and store.
-- | Using AST from inf222-2021-lec0502-typing/ExtendedBTLAST.hs
-- | Extended from inf222-2021-lec0602-interpretation/EnvironmentExtendedBTLAST
--
-- Magne Haveraaen, 2021-02-12

module EvalBstAst where

-- Import Extended BTL AST from inf222-2021-lec0502-typing
import ExtendedBTLAST

-- Import unsigned integers (Modulus integers)
import Data.Word (Word64, Word32, Word8)
-- Import two's complement integers
import Data.Int (Int64, Int16, Int8)
-- Import array datatypes
import Data.Array

-- | Extended BTL abstract syntax, imported from ExtendedBTLAST
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

--------------------------
-- | Value domain to cater for integer and bool types
data ValueDomain = VDInt Int64 | VDBool Word8 
  deriving (Show, Eq, Read)

-- | Encode booleans as Word8
booltovd :: Bool -> ValueDomain
booltovd False = VDBool 0
booltovd True =  VDBool 1
-- | Decode booleans from Word8
vdtobool :: ValueDomain -> Bool
vdtobool (VDBool 0) = False 
vdtobool (VDBool 1) = True 
vdtobool vd = error $ "Wrong value in place of VDBool: " ++ (show vd)

--------------------------
-- | Environment: an association list mapping variables names to location
type Environment = [(String,Location)]
findvar :: String -> Environment -> Location
findvar name ((vname,loc):env) = 
  if name == vname then loc else findvar name env
findvar name [] = error $ "Variable " ++ name ++ " not found"
-- | Store: an array mapping locations to values
type Store = Array Location ValueDomain
-- | Locations are 8 bit unsigned integers
type Location = Word8

-- | Create an empty store and empty environment
newcontext :: (Environment,Store)
newcontext = ([],array (0,maxBound) [(i,VDBool 0)|i<-[0..maxBound]])
-- | Add a new variable
addvariable :: String -> (Environment,Store) -> (Environment,Store)
addvariable name (env,store) = ((name,fromIntegral(length env)):env,store)
-- | Update variable in store
updvariable :: String -> ValueDomain -> (Environment,Store) -> (Environment,Store)
updvariable name val (env,store) = 
  (env, store // [(findvar name env,val)])
-- | Get value of variable in store
getvalue :: String -> (Environment,Store) -> ValueDomain
getvalue name (env,store) = store ! findvar name env


--------------------------
-- | Evaluator with standard functions and variable environment into value domain
eval :: Expr -> Environment -> Store -> ValueDomain
eval (UPlus e1) env store = eval e1 env store
eval (UMinus e1) env store = VDInt (-i) where VDInt i = (eval e1 env store)
eval (UNot e1) env store = VDBool (1 - b1)
  where VDBool b1 = eval e1 env store
eval (IntLiteral i) env store = VDInt (fromInteger i)
eval (BoolLiteral b) env store = booltovd b
eval (VarId name) env store = store ! findvar name env
eval (FunctionCall "false" []) env store = booltovd False
eval (FunctionCall "true" []) env store = booltovd True
eval (FunctionCall "odd" [e1]) env store = 
  booltovd (mod i 2 == 1) where VDInt i = eval e1 env store
eval (FunctionCall "abs" [e1]) env store = 
  VDInt (abs i) where VDInt i = eval e1 env store
eval (FunctionCall "sqr" [e1]) env store = 
  VDInt (i*i) where VDInt i = eval e1 env store
eval (FunctionCall "succ" [e1]) env store = VDInt (i+1) 
  where VDInt i = eval e1 env store
eval (FunctionCall "pred" [e1]) env store = VDInt (i-1) 
  where VDInt i = eval e1 env store
eval (FunctionCall "maxint" []) env store = VDInt maxBound
eval (FunctionCall name args) env store = 
  error $ "Not a standard function: " ++ name
eval (BinaryExpr Plus e1 e2) env store = VDInt (i1 + i2) 
  where
    VDInt i1 = (eval e1 env store)
    VDInt i2 = (eval e2 env store)
eval (BinaryExpr Minus e1 e2) env store = VDInt (i1 - i2) 
  where
    VDInt i1 = (eval e1 env store)
    VDInt i2 = (eval e2 env store)
eval (BinaryExpr Or e1 e2) env store = VDBool $ signum(b1 + b2) 
  where
    VDBool b1 = (eval e1 env store)
    VDBool b2 = (eval e2 env store)
eval (BinaryExpr Mult e1 e2) env store = VDInt (i1 * i2) 
  where
    VDInt i1 = (eval e1 env store)
    VDInt i2 = (eval e2 env store)
eval (BinaryExpr Div e1 e2) env store = VDInt (i1 `div` i2) 
  where
    VDInt i1 = (eval e1 env store)
    VDInt i2 = (eval e2 env store)
eval (BinaryExpr Mod e1 e2) env store = VDInt (i1 `mod` i2) 
  where
    VDInt i1 = (eval e1 env store)
    VDInt i2 = (eval e2 env store)
eval (BinaryExpr And e1 e2) env store = VDBool (i1 * i2) 
  where
    VDBool i1 = (eval e1 env store)
    VDBool i2 = (eval e2 env store)
eval (BinaryExpr Eq e1 e2) env store = booltovd (i1 == i2)
  where
    VDInt i1 = (eval e1 env store)
    VDInt i2 = (eval e2 env store)
eval (BinaryExpr Lt e1 e2) env store = booltovd (i1 < i2)
  where
    VDInt i1 = (eval e1 env store)
    VDInt i2 = (eval e2 env store)
eval (BinaryExpr Gt e1 e2) env store = booltovd (i1 > i2)
  where
    VDInt i1 = (eval e1 env store)
    VDInt i2 = (eval e2 env store)
eval (BinaryExpr Ne e1 e2) env store = booltovd (i1 /= i2)
  where
    VDInt i1 = (eval e1 env store)
    VDInt i2 = (eval e2 env store)
eval (BinaryExpr Le e1 e2) env store = booltovd (i1 <= i2)
  where
    VDInt i1 = (eval e1 env store)
    VDInt i2 = (eval e2 env store)
eval (BinaryExpr Ge e1 e2) env store = booltovd (i1 <= i2)
  where
    VDInt i1 = (eval e1 env store)
    VDInt i2 = (eval e2 env store)
eval (IfExpr b e1 e2) env store = 
  if vdtobool (eval b env store) 
  then eval e1 env store 
  else eval e2 env store



--------------------------
-- | Evaluate examples
testeval = do
    let ex0 = FunctionCall "maxint" []
    let (env,store) = newcontext
    print $ (show $ eval ex0 env store) ++ "== (eval (" ++ (show ex0) ++ ") )"
    --
    let context = (addvariable "a" (addvariable "b" (addvariable "c" (addvariable "d" newcontext))))
    let (env,store) = updvariable "a" (VDInt 12) $ updvariable "b" (VDInt 7) $ updvariable "c" (VDInt 23) $ updvariable "d" (VDInt 127) context
    print $ show $ env
    print $ show $ store
    -- 
    print $ (show $ eval ex1 env store) ++ " == (eval (" ++ (show ex1) ++ ") )"
    print $ (show $ eval ex2 env store) ++ " == (eval (" ++ (show ex2) ++ ") )"
    print $ (show $ eval ex3 env store) ++ " == (eval (" ++ (show ex3) ++ ") )"
    -- print $ (show $ eval ex4 env store) ++ " == (eval (" ++ (show ex5) ++ ") )"
    -- print $ (show $ eval ex5 env store) ++ " == (eval (" ++ (show ex6) ++ ") )"
    print $ (show $ eval ex6 env store) ++ " == (eval (" ++ (show ex6) ++ ") )"
    print $ (show $ eval ex7 env store) ++ " == (eval (" ++ (show ex7) ++ ") )"
    print $ (show $ eval ex8 env store) ++ " == (eval (" ++ (show ex8) ++ ") )"

{-
    let env = [("x",VDBool 1)]
    print $ (show $ eval bad1 env) ++ "== (eval (" ++ (show bad1) ++ ") )"
    let env = [("x",VDInt 12)]
    print $ (show $ eval bad1 env) ++ "== (eval (" ++ (show bad1) ++ ") )"
    let env = []
    print $ (show $ eval bad2 env) ++ "== (eval (" ++ (show bad2) ++ ") )"
    print $ (show $ eval bad3 env) ++ "== (eval (" ++ (show bad3) ++ ") )"
-}


--------------------------
-- | Some example terms in addition to those in ExtendedBTLAST

-- build term for: 12*7 + 23*127
ex6 :: Expr
ex6 = tbin Plus (tbin Mult (tint 12) (tint 7)) (tbin Mult (tint 231) (tint 127))

-- build term for: (12*7 + 23) * 127
ex7 :: Expr
ex7 = tbin Mult (tbin Plus  (tbin Mult (tint 12) (tint 7)) (tint 23)) (tint 127)

-- build term for: if (23*33 ≤ 33) then 44 else 55
ex8 :: Expr
ex8 = tife (tbin Le (tbin Mult (tint 23) (tint 33)) (tint 33)) (tint 44) (tint 55)


-- build bad term: -(not(9))
bad2 :: Expr
bad2 = tum (tun (tint 9))
-- build bad term: -(not(false))
bad3 :: Expr
bad3 = tum (tun (tboo False))

