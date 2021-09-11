-- | AST and examples for simplified Pascal style procedures
--
-- Author Magne Haveraaen
-- Since 2021-02-22

module SimpleProcedure where

-- Uses extended BTL expression AST from L0502
import ExtendedBTLAST

-- Uses typing framework from L0502
import ExtendedBTLDeclarations

-- Uses extended BIPL statements and interpreters from L0602
import EvalBstAst
import InterpretBiplAst

--------------------------
-- | AST for simplified procedure declarations, see Pascal User Manual and Report (LNCS18).
{-
<procedure declaration> ::= <procedure heading> <block>

<procedure heading> ::= 
    procedure <identifier> ( <formal parameter section> {; <formal parameter section>} )

<formal parameter section> ::= <parameter group> | var <parameter group>

<parameter group> ::= <identifier> {, <identifier> } : <type identifier>

<block> ::= <variable declaration part> <statement part>

<variable declaration part> ::=
    <identifier> {, <identifier> } : <type> ;
    { <identifier> {, <identifier> } : <type> ; }

<statement part> ::= <statement>
-}
data Proc = ProcedureDeclaration 
    String -- Name of the procedure
    [Parameter] -- Parameter list
    [VarType] -- Local variables
    Stmt -- Statement part
    deriving (Show, Eq, Read)


-- | Characterisation of a simplified procedure's parameters: 
-- First component is whether the parameter is a reference (var keyword) or not (value component).
-- The second component is the variable name and type.
type Parameter = (Bool, VarType)
-- | Extracts the list of variable names from a parameter list
extractParameterNames :: [Parameter] -> [String]
extractParameterNames params = map (fst . snd) params
-- | Extracts the list of reference variable names from a parameter list
extractReferenceParameterNames :: [Parameter] -> [String]
extractReferenceParameterNames params = [ vname | (ref,(vname,vtype)) <- params, ref ]


--------------------------
-- | Standard functions from Pascal. 
-- The declarations are needed for type checking
simplifiedPascalStandardFunctions :: [FunType]
simplifiedPascalStandardFunctions = [
     ("false",([],TBool)), ("true",([],TBool)),
     ("odd",([TInt],TBool)), 
     ("abs",([TInt],TInt)), ("sqr",([TInt],TInt)), ("succ",([TInt],TInt)), ("pred",([TInt],TInt)),
     ("maxint",([],TInt))
    ]

--------------------------
-- | Perform a procedure declaration: take a list of argument values, pass them to the procedure interpreter, and gather the return values.
-- | Internally perform 
-- • sets up the execution environment for the <statement part>, 
-- • copies the argument values into the store
-- • interprets the procedure in this environment,
-- • gathers the resulting values of the reference parameters and returns this list.
perform :: Proc -> Args -> Rets
perform proc args = rets
    where
    ProcedureDeclaration pname params lvars stmt = proc
    (env,store) = allocateParameterAndValue (extractParameterNames params) args newcontext
    (env',store') = allocateLocalVariables lvars (env,store)
    store'' = exec stmt env' store'
    rets = extractValuesFromStore (extractReferenceParameterNames params) env store''
    -- rets = returnproc params env store''

-- | List of actual argument values to parameters
type Args = [ValueDomain]
-- | List of return values from reference parameters
type Rets = [ValueDomain]

--------------------------
-- 4.3.3
-- 1. Methods implemented below
-- 2. The tests pass
-- | Allocates variable names and inserts their argument values into the store.
allocateParameterAndValue :: [String] -> [ValueDomain] -> (Environment,Store) -> (Environment,Store)
allocateParameterAndValue [] _ (env,store) = (env,store)
allocateParameterAndValue _ [] (env,store) = (env,store)
allocateParameterAndValue [vname] [val] (env,store) = updvariable vname val (addvariable vname (env,store))
allocateParameterAndValue (vname:vnames) (val:vals) (env,store) = do
    let context = updvariable vname val (addvariable vname (env,store))
    allocateParameterAndValue vnames vals context

-- | From a list of variables extract their values from the store 
extractValuesFromStore :: [String] -> Environment -> Store -> Rets
extractValuesFromStore vnames env store = map (\vname -> getvalue vname (env, store)) vnames 

-- | Takes a list of local variable declarations and allocates them in the store.
allocateLocalVariables :: [VarType] -> (Environment,Store) -> (Environment,Store)
allocateLocalVariables [] (env,store) = (env,store)
allocateLocalVariables [(vname, vtype)] (env,store) = addvariable vname (env,store) 
allocateLocalVariables ((vname,vtype):vdecls) (env,store) = do
    let context = addvariable vname (env,store)
    allocateLocalVariables vdecls context

--------------------------
{-
   EXAMPLES
-}
--------------------------
-- | Procedure for Euclidean division. 
-- The quotient of x and y is assigned to q while the remainder of x and y is assigned to r.
{-
    procedure eucliddiv ( x,y:integer, var q,r:integer );
    begin
    q := 0;
    r := x;
    while y <= r do
        begin
        r := r - y;
        q := q + 1;
        end;
    end;
-}
-- The eucliddiv_stmt statement is taken from InterpretBiplAst.
eucliddiv_proc :: Proc
eucliddiv_proc = ProcedureDeclaration
    "eucliddiv"
    [(False,("x",TInt)),(False,("y",TInt)),
     (True,("q",TInt)),(True,("r",TInt))]
    []
    eucliddiv_stmt

eucliddiv_run :: Integer -> Integer -> (Integer,Integer)
eucliddiv_run x y = (toInteger r, toInteger q)
    where 
        [VDInt r,VDInt q] = 
            perform eucliddiv_proc [VDInt (fromInteger x),VDInt (fromInteger y), VDInt 0, VDInt 0]

unittest_eucliddiv = do
    let check = [ eucliddiv_run x y == divMod x y | x<-[0..100], y <- [1..100] ]
    let ok = foldl (&&) (True) check
    print $ if ok then "Euclidean division tests passed!" else "Euclidean division failed!"



--------------------------
-- | Computus
{-
    (** Computing Easter Day for year Y using "Anonymous Gregorian algorithm". *)
    procedure computus ( Y:integer; var month,day:integer ) ;
    var a,b,c,d,e,f,g,h,i,k,l,m,n,o:integer;
    begin
    a := Y mod 19;
    b := Y div 100;
    c := Y mod 100;
    d := b div 4;
    e := b mod 4;
    f := (b + 8) div 25;
    g := (b - f + 1) div 3;
    h := (19*a + b - d - g + 15) mod 30;
    i := c div 4;
    k := c mod 4;
    l := (32 + 2*e + 2*i - h - k) mod 7;
    m := (a + 11*h + 22*l) div 451;
    n := (h + l - 7*m + 114) div 31;
    o := (h + l - 7*m + 114) mod 31;
    month := n;
    day := o + 1;
    end ;
-}
computus_proc :: Proc
computus_proc = ProcedureDeclaration
  "computus"
  [(False,("Y",TInt)),
   (True,("month",TInt)),
   (True,("day",TInt))]
  (varType ["a","b","c","d","e","f","g","h","i","k","l","m","n","o"] TInt)
  computus_stmt
computus_stmt :: Stmt 
computus_stmt = Block [
    Assign "a" (BinaryExpr Mod (VarId "Y")(IntLiteral 19)),
    Assign "b" (BinaryExpr Div (VarId "Y")(IntLiteral 100)),
    Assign "c" (BinaryExpr Mod (VarId "Y")(IntLiteral 100)),
    Assign "d" (BinaryExpr Div (VarId "b")(IntLiteral 4)),
    Assign "e" (BinaryExpr Mod (VarId "b")(IntLiteral 4)),
    Assign "f" (BinaryExpr Div (BinaryExpr Plus (VarId "b")(IntLiteral 8))(IntLiteral 25)),
    Assign "g" (BinaryExpr Div (BinaryExpr Plus (BinaryExpr Minus (VarId "b")(VarId "f"))(IntLiteral 1))(IntLiteral 3)),
    Assign "h" (BinaryExpr Mod hexp (IntLiteral 30)),
    Assign "i" (BinaryExpr Div (VarId "c")(IntLiteral 4)),
    Assign "k" (BinaryExpr Mod (VarId "c")(IntLiteral 4)),
    Assign "l" (BinaryExpr Mod lexp (IntLiteral 7)),
    Assign "m" (BinaryExpr Div (BinaryExpr Plus (BinaryExpr Plus (VarId "a")(BinaryExpr Mult (IntLiteral 11)(VarId "h")))(BinaryExpr Mult (IntLiteral 22)(VarId "l")))(IntLiteral 451)),
    Assign "n" (BinaryExpr Div (BinaryExpr Plus (BinaryExpr Minus (BinaryExpr Plus (VarId "h")(VarId "l"))(BinaryExpr Mult (IntLiteral 7)(VarId "m")))(IntLiteral 114))(IntLiteral 31)),
    Assign "o" (BinaryExpr Mod (BinaryExpr Plus (BinaryExpr Minus (BinaryExpr Plus (VarId "h")(VarId "l"))(BinaryExpr Mult (IntLiteral 7)(VarId "m")))(IntLiteral 114))(IntLiteral 31)),
    Assign "month" (VarId "n"),
    Assign "day" (BinaryExpr Plus (VarId "o")(IntLiteral 1))
    ]
hexp = (BinaryExpr Plus(BinaryExpr Minus (BinaryExpr Minus (BinaryExpr Plus (BinaryExpr Mult (IntLiteral 19)(VarId "a"))(VarId "b"))(VarId "d"))(VarId "g"))(IntLiteral 15))
lexp = (BinaryExpr Minus(BinaryExpr Minus (BinaryExpr Plus (BinaryExpr Plus (IntLiteral 32)(BinaryExpr Mult (IntLiteral 2)(VarId "e")))(BinaryExpr Mult (IntLiteral 2)(VarId "i")))(VarId "h"))(VarId "k"))

computus_run :: Integer -> (Integer,Integer,Integer)
computus_run y = (toInteger y, toInteger month, toInteger day)
    where 
        [VDInt month,VDInt day] = 
            perform computus_proc [VDInt (fromInteger y), VDInt 0, VDInt 0]
unittest_computus = do
    let ok = computus_run 2021 == (2021,4,4)
          && computus_run 2020 == (2020,4,12)
          && computus_run 2019 == (2019,4,21)
          && computus_run 2008 == (2008,3,23)
          && computus_run 2011 == (2011,4,24)
          && computus_run 2038 == (2038,4,25)
    print $ if ok then "Computus tests passed!" else "Computus failed!"

--------------------------
-- | Procedure with initialisation problem.
{-
    procedure init_problem ( var x:integer ) ;
    var y:integer;
    begin
    if (x <> 0) and (x*x = 0)
    then x := y
    else x := pred(x);
    end ;
-}

-- 4.4.1
-- 1. The test fails because: Int16 makes the test fail because of integer overflow.
-- 2. 
-- 3. Yes. When we change Int16 to Int64 the test passes correctly, becuase interger overflow is not triggered.
initproblem_proc :: Proc
initproblem_proc = ProcedureDeclaration
  "init_problem"
  [(True,("x",TInt))]
  [("y",TInt)]
  (Block [
      IfStmt (BinaryExpr And 
                (BinaryExpr Ne(VarId "x")(IntLiteral 0))
                (BinaryExpr Eq(BinaryExpr Mult(VarId "x")(VarId "x"))(IntLiteral 0)))
            (Assign "x" (VarId "y"))
            (Assign "x"(FunctionCall "pred" [(VarId "x")]))
  ])
initproblem_run :: ValueDomain -> ValueDomain 
initproblem_run x = head (perform initproblem_proc [x])
unittest_initproblem = do
    let check = [ initproblem_run (VDInt x) == VDInt (x-1) | x<-[-32768..32767]]
    let check' = filter (\x -> initproblem_run (VDInt x) /= VDInt (x-1)) [-32768..32767]  
    mapM_ print check'
    let ok = foldl (&&) (True) check
    print $ if ok then "Initialisation problem tests passed!" else "Initialisation problem failed!"