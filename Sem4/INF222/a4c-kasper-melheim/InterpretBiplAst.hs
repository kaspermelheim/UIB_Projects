-- | inf222-2021-lec0602-interpretation
-- | Interpretation function for BIPL with environment and store.
-- | Using evaluator for BTL from EvalBstAst.hs
--
-- Magne Haveraaen, 2021-02-12

module InterpretBiplAst where

-- Import Extended BTL AST from inf222-2021-lec0502-typing
import ExtendedBTLAST
import EvalBstAst

--------------------------
-- | BIPL syntax with Extended BTL imported from ExtendedBTLAST
{- |
Symbol assign : string × expr → stmt ;
-- x := e
Symbol block : stmt* → stmt ;
-- begin … end
Symbol ifstmt : expr × stmt × stmt → stmt ;
-- if cond then s1 else s2
Symbol while : expr × stmt → stmt ;
-- while cond do s1
-}
data Stmt
    = Assign String Expr
    | Block [Stmt]
    | IfStmt Expr Stmt Stmt
    | While Expr Stmt
    deriving (Show, Eq, Read)

--------------------------
-- | Executing a statement: a store transformation in an environment
exec :: Stmt -> Environment -> Store -> Store
exec (Assign name exp) env store = store'
    where (env',store') = updvariable name (eval exp env store) (env,store)
exec (Block (stmt:stmts)) env store =
    exec (Block stmts) env (exec stmt env store)
exec (Block []) env store = store
exec (IfStmt cond s1 s2) env store =
    if vdtobool (eval cond env store) 
        then exec s1 env store 
        else exec s2 env store
exec (While cond stmt) env store =
    if vdtobool (eval cond env store)
        then exec (While cond stmt) env (exec stmt env store)
        else store


--------------------------
-- | Simple test programs
testexec = do
    -- Creating the store with variables and preassigned values.
    let context = addvariable "x" (addvariable "y" newcontext )
    let (env,store) = updvariable "x" (VDInt 5) $ updvariable "y" (VDInt 6) context
    let (env',store') = updvariable "y" (VDInt 27) (env,store)
    print $ "store: x=" ++ (show $ getvalue "x" (env, store))
    print $ "store: y=" ++ (show $ getvalue "y" (env, store))
    print $ "store': x=" ++ (show $ getvalue "x" (env, store'))
    print $ "store': y=" ++ (show $ getvalue "y" (env, store'))
    -- Setting the value of variable "x"
    let stmtx = Assign "x" (IntLiteral 87)
    let stmtxstore = exec stmtx env store
    let stmtxstore' = exec stmtx env store'
    print $ "stmtxstore: x=" ++ (show $ getvalue "x" (env, stmtxstore))
    print $ "stmtxstore: y=" ++ (show $ getvalue "y" (env, stmtxstore))
    print $ "stmtxstore': x=" ++ (show $ getvalue "x" (env, stmtxstore'))
    print $ "stmtxstore': y=" ++ (show $ getvalue "y" (env, stmtxstore'))
    let stmtxy = Block [stmtx, Assign "y" (BinaryExpr Mult (VarId "x") (VarId "y"))]
    let stmtxystore = exec stmtxy env store
    let stmtxystore' = exec stmtxy env store'
    print $ "stmtxystore: x=" ++ (show $ getvalue "x" (env, stmtxystore))
    print $ "stmtxystore: y=" ++ (show $ getvalue "y" (env, stmtxystore))
    print $ "stmtxystore': x=" ++ (show $ getvalue "x" (env, stmtxystore'))
    print $ "stmtxystore': y=" ++ (show $ getvalue "y" (env, stmtxystore'))


--------------------------
{- | Power function from Pascal User Manual page 81 (LNCS18)
function power(x:real: y:integer): real; 
  {y>=O} 
  var z : real;
  begin
  z := 1 ;
  while y > 0 do
    begin
    while not odd(y) do
      begin
      y := y div 2;
      x := sqr(x);
      end;
    y := y - 1;
    z := x*z;
    end;
  power ::= z
  end
-}
-- | The algorith from the body of the "power" function
power_stmt = 
    Block [
    Assign "z" (IntLiteral 1),
    While (BinaryExpr Gt (VarId "y") (IntLiteral 0))
        (Block [
        While (UNot (FunctionCall "odd" [VarId "y"]))
            (Block [
            Assign "y" (BinaryExpr Div (VarId "y") (IntLiteral 2)),
            Assign "x" (FunctionCall "sqr" [VarId "x"])
            ]),
        Assign "y" (FunctionCall "pred" [VarId "y"]),
        Assign "z" (BinaryExpr Mult (VarId "x") (VarId "z"))
        ])
    ]

-- | BIPL version of power uses only integers
-- Set up context with two variables "x" and "y"
power_context = addvariable "x" (addvariable "y" newcontext)
-- | Call power function with 2 arguments: 
-- declare local variable "z", execute power statement (body of function), and return result from "z"
call_power x y = 
    getvalue "z" (env, 
        exec power_stmt env 
            (snd $ updvariable "x" (VDInt x) 
                 $ updvariable "y" (VDInt y) (env,store)))
    where (env,store) = addvariable "z" $ power_context
-- | Test program for power function
testpower = do
    print $ "2^14 == " ++ (show $ call_power 2 14)
    print $ "2^15 == " ++ (show $ call_power 2 15)
    print $ "2^16 == " ++ (show $ call_power 2 16)
    print $ "10^4 == " ++ (show $ call_power 10 4)
    print $ "10^5 == " ++ (show $ call_power 10 5)
    print $ "10^18 == " ++ (show $ call_power 10 18)
    print $ "2^62 == " ++ (show $ call_power 2 62)
    print $ "2^63 == " ++ (show $ call_power 2 63)
    print $ "2^64 == " ++ (show $ call_power 2 64)


--------------------------
-- | Euclidean division: an algorithm that computes div&mod using only Plus/Minus.
-- The inputs are in variables "x" (14) and "y" (4), the resulting quotient in "q" and remainder in "r".
eucliddiv_stmt =
    -- Assign "x" $ Intliteral 14,
    -- Assign "y" $ Intliteral 4,
  Block [
    Assign "q" $ IntLiteral 0,
    Assign "r" $ VarId "x",
    While (BinaryExpr Le (VarId "y") (VarId "r"))
      (Block [
        Assign "r" ((BinaryExpr Minus (VarId "r") (VarId "y"))),
        Assign "q" ((BinaryExpr Plus (VarId "q") (IntLiteral 1)))
      ])
  ]

-- | Set up context with input variables "x" and "y" and output variables "q" and "r".
eucliddiv_context = addvariable "q" $ addvariable "r" $ addvariable "x" (addvariable "y" newcontext)
-- | Call power function with 2 arguments: 
-- execute eucliddiv statement (body of function), and return result from variables "q" and "r" variables.
call_eucliddiv x y = (q,r)
    where 
        -- Update input argument values in context
        (env,store) = updvariable "x" (VDInt x) 
                 $ updvariable "y" (VDInt y) eucliddiv_context
        -- Compute
        store' = exec eucliddiv_stmt env store
        -- Extract results
        VDInt q = getvalue "q" (env,store')
        VDInt r = getvalue "r" (env,store')

-- | Comparison function calling div and mod from EBTL.
call_divmod x y = (d,m)
    where
        (env,store) = newcontext 
        VDInt d = eval (BinaryExpr Div (IntLiteral x) (IntLiteral y)) env store
        VDInt m = eval (BinaryExpr Mod (IntLiteral x) (IntLiteral y)) env store

-- | Test program for euclidean division function
testeucliddiv = do
    print $ call_eucliddiv 14 4
    print $ call_divmod    14 4
    --
    print $ call_eucliddiv 45 11
    print $ call_divmod    45 11

