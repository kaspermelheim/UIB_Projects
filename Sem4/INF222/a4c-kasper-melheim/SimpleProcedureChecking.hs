module SimpleProcedureChecking where

import SimpleProcedure
import WellTypedAST
import EvalBstAst
import ExtendedBTLAST
import ExtendedBTLDeclarations
import InterpretBiplAst
import Data.List

-- 1

-- Type checking the procedure: build the type environment and check the statements.
typeCheckProc :: [FunType] -> Proc -> Bool
typeCheckProc ftypes (ProcedureDeclaration str param vtypes stmt) = typeCheckStmt (ftypes, vtypes) stmt

-- Type checking the statements.
typeCheckStmt :: Declarations -> Stmt -> Bool
typeCheckStmt decls@(ftypes,vtypes) (Assign str expr) = (findVarType str vtypes) == (typeCheck decls expr)
typeCheckStmt decls@(ftypes,vtypes) (IfStmt expr stmt stmt2) = if (typeCheck decls expr) == TBool 
                                                                    then (typeCheckStmt decls stmt) && (typeCheckStmt decls stmt2) 
                                                               else error "Not a bool"
typeCheckStmt decls@(ftypes,vtypes) (While expr stmt) = if (typeCheck decls expr) == TBool
                                                            then (typeCheckStmt decls stmt) 
                                                        else error "Not a bool"
-- Alternate solution
typeCheckStmt decls@(ftypes,vtypes) (Block stmt) = foldl (&&) True [typeCheckStmt decls s | s <- stmt]

-- 2

-- Checking the procedure: no duplicate declarations in parameter list and local variables.
variableCheckProc :: Proc -> Bool
variableCheckProc (ProcedureDeclaration str param vtypes stmt) = length list == length (nub list) where 
                                                                list = vtypes ++ map snd param

-- 3
-- Checking the procedure: no use of uninitialised variables and checking that all variables have been declared.
initialisedCheckProc :: Proc -> Bool
initialisedCheckProc (ProcedureDeclaration str param vtypes (Assign str2 expr)) = if elem str2 (map fst vtypes) || elem str2 (map fst (map snd param)) 
                                                                                        then True
                                                                                  else error ("Unknown variable" ++ str)
initialisedCheckProc (ProcedureDeclaration str param vtypes (IfStmt expr stmt1 stmt2)) = initialisedCheckProc (ProcedureDeclaration str param vtypes stmt1) && initialisedCheckProc (ProcedureDeclaration str param vtypes stmt2)
initialisedCheckProc (ProcedureDeclaration str param vtypes (Block stmts)) = foldl (&&) True [initialisedCheckProc (ProcedureDeclaration str param vtypes stmt) | stmt <- stmts]
initialisedCheckProc (ProcedureDeclaration str param vtypes (While expr stmt)) = initialisedCheckProc (ProcedureDeclaration str param vtypes stmt)

-- 4
-- Doing a complete safety check of a procedure
-- Type correctness
-- Variables declared before use
-- No dublicate declarations
-- No use before initialisation
safetyCheck :: Proc -> Bool
safetyCheck (ProcedureDeclaration str param vtypes stmt) = undefined
