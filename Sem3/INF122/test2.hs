import Data.Char

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

--parseExpr recursively goes through list and produces ast
parseExpr :: [String] -> (Ast,[String])
parseExpr [] = error "Error!"
parseExpr (s:ss) | all isDigit s = (Num (read s),ss)
             | s == "-" = let (e,ss') = parseExpr ss in (Minus e e',ss')
             | s == "*" = (Mult e e',ss'')
             | s == "+" = (Plus e e',ss'') where
                          (e,ss') = parseExpr ss
                          (e',ss'') = parseExpr ss'

parseExpr2 :: [String] -> (Ast, [String])
parseExpr2 ts
  =  let (f1, ts1) = parseTerm ts
     in  go f1 ts1
  where go acc (op:ts2)
          | op == "+" || op == "-"
          = let (f2, ts3) = parseTerm ts2
            in go ((astOp op) acc f2) ts3
        go acc rest = (acc, rest)
        astOp "+" = Plus
        astOp "-" = Minus
-- parse returns the first in the tuple returned from parseExpr
parse :: String -> Ast
parse [] = error "Empty string"
parse str = fst $ parseExpr x
  where x = tokenize str

parse :: String -> Ast
parse x =
  case parseMinus (tokenize x) of
    (i, []) -> i
    (_, j : _) -> error ("unexpected token " ++ (show j))