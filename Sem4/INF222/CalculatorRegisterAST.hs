-- AST for simple integer calculator.
-- 
-- Author Magne Haveraaen
-- Since 2020-03-14
module CalculatorRegisterAST where

import Data.Array


-- | Expressions for a simple calculator.
-- The calculator supports literals and operations
-- Addition, multiplication, and subtraction/negation.

data CalcExprAST
    = Lit Integer
    | Add CalcExprAST CalcExprAST
    | Mult CalcExprAST CalcExprAST
    | Sub CalcExprAST CalcExprAST
    | Neg CalcExprAST
    | Reg Register
    deriving (Eq, Read, Show)

-- | Statement for setting a register
data CalcStmtAST
    = SetReg Register CalcExprAST
    deriving (Eq, Read, Show)

-- | Enumeration of the 10 registers.
data Register
    = Reg0
    | Reg1
    | Reg2
    | Reg3
    | Reg4
    | Reg5
    | Reg6
    | Reg7
    | Reg8
    | Reg9
    deriving (Eq, Read, Show)

-- | A Store for a register calculator is an array with 10 integer elements.
-- The access functions getregister/setregister need to translate between register and array index.
type Store = Array Integer Integer

-- | Defines a store for 10 registers
registerstore :: Store
registerstore = array (0,9) [( i ,0) | i <-[0..9]]

-- | Get the value stored for the given register.
getstore :: Store -> Integer -> Integer
getstore store ind =
    if 0 <= ind && ind < 10
        then store ! ind
    else error $ "Not a register ␣index␣" ++ (show ind)

-- | Set the value stored for the given register.
setstore :: Integer -> Integer -> Store -> Store
setstore ind val store =
    if 0 <= ind && ind < 10
        then store // [( ind , val ) ]
    else error $ "Not a register index " ++ (show ind) ++ " for " ++ (show val)

eval :: CalcExprAST -> Store -> Integer
eval (Lit a) store = a
eval (Add a b ) store = eval a store + eval b store
eval (Mult a b) store = eval a store * eval b store
eval (Sub a b) store = eval a store - eval b store
eval (Neg a) store = - eval a store
eval (Reg a) store = getstore store (getRegisterIndex a)
eval instr store = error $ ("Unknown intruction: " ++ show instr)

execute :: CalcStmtAST -> Store -> Store
execute (SetReg reg exp) store = setstore (getRegisterIndex reg) (eval exp store) store

getRegisterIndex :: Register -> Integer
getRegisterIndex Reg0 = 0
getRegisterIndex Reg1 = 1
getRegisterIndex Reg2 = 2
getRegisterIndex Reg3 = 3
getRegisterIndex Reg4 = 4
getRegisterIndex Reg5 = 5
getRegisterIndex Reg6 = 6
getRegisterIndex Reg7 = 7
getRegisterIndex Reg8 = 8
getRegisterIndex Reg9 = 9



-- | A few ASTs for register based CalcExprAST.

calculatorRegisterAST1 = Lit 4
calculatorRegisterAST2 = Neg (Mult (Add (Lit 3) (Sub ( Lit 7) ( Lit 13) ) ) ( Lit 19) )
calculatorRegisterAST3 = Add (Reg Reg1) (Reg Reg4)
calculatorRegisterAST4 = Reg Reg2

-- | A few ASTs for setting registers CalcStmtAST.
calculatorSetRegisterAST1 = SetReg Reg4 calculatorRegisterAST1
calculatorSetRegisterAST2 = SetReg Reg1 calculatorRegisterAST2
calculatorSetRegisterAST3 = SetReg Reg2 calculatorRegisterAST3
calculatorSetRegisterAST4 = SetReg Reg1 calculatorRegisterAST4

-- | Unit test: show some calculator ASTs and their evaluation (commented out) and
-- validate those against expected values.
unittestCalculatorRegisterInterpreter :: IO ()
unittestCalculatorRegisterInterpreter = do
    print $ "−- unittestCalculatorRegisterInterpreter "

    let store = setstore ( getRegisterIndex Reg4) 43 ( setstore ( getRegisterIndex Reg2) 21 ( setstore ( getRegisterIndex Reg1) 11 registerstore ) )

    let store1 = execute (SetReg Reg1 ( Lit 11) ) registerstore
    let store2 = execute (SetReg Reg2 (Add (Reg Reg1) ( Lit 10) ) ) store1
    let store3 = execute (SetReg Reg4 (Sub (Mult (Reg Reg2) ( Lit 2) ) ( Lit (-1))) ) store2


    print $
        if (4 == (eval calculatorRegisterAST1 store ) )
        && (57 == (eval calculatorRegisterAST2 store ) )
        && (54 == (eval calculatorRegisterAST3 store ) )
        && (21 == (eval calculatorRegisterAST4 store ) )
        && (store == store3)
        && (4 == eval (Reg Reg4) ( execute calculatorSetRegisterAST1 registerstore ) )
        && (57 == eval (Reg Reg1) ( execute calculatorSetRegisterAST2 registerstore ) )
        && (0 == eval (Reg Reg2) ( execute calculatorSetRegisterAST3 registerstore ) )
        && (0 == eval (Reg Reg1) ( execute calculatorSetRegisterAST4 registerstore ) )
        then "Unit tests hold"
    else "Tests failed "

-- | Interactive calculator.
-- At the prompt provide a (Haskell) CalcExprAST and see how it is evald.
main :: IO ()
main = do
    print $ "-- Interactive register calulator ."
    mainCalculatorRegisterAsk registerstore

mainCalculatorRegisterAsk state = do
    putStr $ "c|"
    str <- getLine
    if str /= ""
    then
        if str == "show"
        then mainCalculatorRegisterShowstate state
        else mainCalculatorRegisterExc str state
    else putStrLn $ "Finished "

-- | Shows current value of state and continues with interactive register calculator.
mainCalculatorRegisterShowstate state = do
    putStrLn $ " state = " ++ (show state)
    mainCalculatorRegisterAsk state

-- | Parses and executes CalcStmtAST and prints subexpression value.
-- Then continues with interactive register calculator.
mainCalculatorRegisterExc str state = do
    -- print $ "str=" ++ (show str)
    let stmt = (read str ) :: CalcStmtAST
    -- print $ "execute(" ++ (show stmt) ++ ") state == " ++ (show $ execute stmt state)
    let SetReg reg expr = stmt
    print $ " evaluate (" ++ (show expr) ++ ") state == " ++ (show $ eval expr state )
    mainCalculatorRegisterAsk $ execute stmt state

