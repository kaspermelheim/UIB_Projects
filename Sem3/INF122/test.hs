import Data.Char

data Token
  = PlusTok 
  | TimesTok
  | OpenTok
  | CloseTok
  | IntTok Int
  | MinusTok
  | StrTok
  deriving (Show, Eq)

data Ast
    = Word String
    | Num Int
    | Mult Ast Ast
    | Plus Ast Ast
    | Minus Ast Ast
    deriving (Eq, Show)

lexer :: String -> [Token]
lexer []              = []
lexer ('+' : restStr) = PlusTok  : lexer restStr
lexer ('-' : restStr) = MinusTok  : lexer restStr
lexer ('*' : restStr) = TimesTok : lexer restStr 
lexer ('(' : restStr) = OpenTok    : lexer restStr 
lexer (')' : restStr) = CloseTok   : lexer restStr
lexer (chr : restStr) 
  | isSpace chr       = lexer restStr
lexer str@(chr : _) 
  | isDigit chr
  = IntTok (stringToInt digitStr) : lexer restStr
  where
     (digitStr, restStr) = break (not . isDigit) str
     -- local function to convert a string to an integer value
     stringToInt :: String -> Int
     stringToInt = foldl (\acc chr -> 10 * acc + digitToInt chr) 0
  -- runtime error for all other characters:
lexer (chr : restString) 
  = error ("lexer: unexpected character: '" ++ (show chr))

collectWhile :: (Char -> Bool) -> String -> (String, String)
collectWhile p s = (takeWhile p s, dropWhile p s)

----

parseInt :: [Token] -> Maybe (Ast, [Token])
parseInt (IntTok n : restTokens)
  = Just (Num n, restTokens)
parseInt tokens
  = Nothing

parseProdOrInt :: [Token] -> Maybe (Ast, [Token])
parseProdOrInt tokens
  = case parseInt tokens of
      Just (expr1, (TimesTok : restTokens1)) -> 
          case parseProdOrInt restTokens1 of
            Just (expr2, restTokens2) -> Just (Mult expr1 expr2, restTokens2)
            Nothing                   -> Nothing
      result -> result     -- could be 'Nothing' or a valid expression

parseIntOrParenExpr :: [Token] -> Maybe (Ast, [Token])
parseIntOrParenExpr (IntTok n : restTokens)
  = Just (Num n,   restTokens)
parseIntOrParenExpr (OpenTok : restTokens1)
  = case parseSumOrProdOrIntOrParenExpr restTokens1 of
       Just (expr, (CloseTok : restTokens2)) -> Just (expr, restTokens2)
       Just _  -> Nothing -- no closing paren
       Nothing -> Nothing
parseIntOrParenExpr tokens
  = Nothing
      
parseProdOrIntOrParenExpr :: [Token] -> Maybe (Ast, [Token])
parseProdOrIntOrParenExpr tokens
  = case parseIntOrParenExpr tokens of
      Just (expr1, (TimesTok : restTokens1)) -> 
          case parseProdOrIntOrParenExpr restTokens1 of
            Just (expr2, restTokens2) -> Just (Mult expr1 expr2, restTokens2)
            Nothing                   -> Nothing
      result -> result   
              
parseSumOrProdOrIntOrParenExpr :: [Token] -> Maybe (Ast, [Token])
parseSumOrProdOrIntOrParenExpr tokens
  = case parseProdOrIntOrParenExpr tokens of
      Just (expr1, (PlusTok : restTokens1)) -> 
          case parseSumOrProdOrIntOrParenExpr restTokens1 of
            Just (expr2, restTokens2) -> Just (Plus expr1 expr2, restTokens2)
            Nothing                   -> Nothing
      result -> result

parseMinusOrSumOrProdOrIntOrParenExpr :: [Token] -> Maybe (Ast, [Token])
parseMinusOrSumOrProdOrIntOrParenExpr tokens
  = case parseSumOrProdOrIntOrParenExpr tokens of
      Just (expr1, (MinusTok : restTokens1)) -> 
          case parseMinusOrSumOrProdOrIntOrParenExpr restTokens1 of
            Just (expr2, restTokens2) -> Just (Minus expr1 expr2, restTokens2)
            Nothing                   -> Nothing
      result -> result

parse :: String -> Ast
parse tokens =
  case parseMinusOrSumOrProdOrIntOrParenExpr (lexer tokens) of
    Just (expr, []) -> expr    
    _               -> error "Could not parse input"

----





data AST =
    Function String [String] [AST]
  | BinOp AST AST AST
  | Pluss
  | FunctionCall String [AST]
  | Variable String
  deriving (Show)

prettyPrint :: Int -> AST -> String
prettyPrint n (Function a b c) = "Function " ++ show a ++ " " ++ show b ++
    foldl (++) "" (map (\x -> "\n" ++ take (n + 1) (repeat '\t') ++
    prettyPrint (n + 1) x) c)
prettyPrint n a = show a

a = (Function "foo" ["x","y"] [FunctionCall "foo" [Variable "x",Variable "y"], BinOp Pluss (FunctionCall "x" []) (FunctionCall "y" [])])