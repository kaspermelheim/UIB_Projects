-- AST for simple integer calculator.
-- 
-- Author Magne Haveraaen
-- Since 2020-03-14
module CalculatorAST where

-- | Expressions for a simple calculator.
-- The calculator supports literals and operations
-- Addition, multiplication, and subtraction/negation.

data CalcExprAST
    = Lit Integer
    | Add CalcExprAST CalcExprAST
    | Mult CalcExprAST CalcExprAST
    | Sub CalcExprAST CalcExprAST
    | Neg CalcExprAST
    deriving (Eq, Read, Show)

-- | A couple ASTs for CalcExprAST.
calculatorAST1 :: CalcExprAST
calculatorAST1 = Lit 4

calculatorAST2 :: CalcExprAST
calculatorAST2 = Neg (Mult (Add (Lit 3) (Sub ( Lit 7) ( Lit 13) ) ) ( Lit 19) )

eval :: CalcExprAST -> Integer
eval (Lit a) = a
eval (Add a b ) = eval a + eval b
eval (Mult a b) = eval a * eval b
eval (Sub a b) = eval a - eval b
eval (Neg a) = - eval a

-- | Unit test: show some calculator ASTs and their evaluation (commented out) and
-- validate those against expected values.
unittestCalculatorInterpreter :: IO ()
unittestCalculatorInterpreter = do
    print $ "−−␣ unittestCalculatorInterpreter "
    -- print $ "evaluate " ++ (show calculatorAST1) ++ " == "
    -- ++ (show $ evaluate calculatorAST1)
    -- print $ "evaluate " ++ (show calculatorAST2) ++ " == "
    -- ++ (show $ evaluate calculatorAST2)
    print $ if (4 == (eval calculatorAST1 ) ) && (57 == (eval calculatorAST2 ) )
            then "Unit␣ tests ␣hold"
            else "Tests␣ failed "

-- | Interactive calculator.
-- At the prompt provide a (Haskell) CalcExprAST and see how it is evaluated.
main :: IO ()
main = do
    print $ "−−␣ Interactive ␣ calulator "
    str <- getLine
    let expr = (read str ) :: CalcExprAST
    print $ " evaluate (" ++ (show expr) ++ ")=" ++ (show $ eval expr)