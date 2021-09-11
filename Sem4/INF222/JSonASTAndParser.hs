module JSonASTAndParser where

import Data.Char
import Control.Applicative

data JSonValue
    = JSonNull
    | JSonBool Bool 
    | JSonNumber Integer -- Note: no support for floats
    | JSonString String 
    | JSonArray [JSonValue]
    | JSonObject [(String, JSonValue)]
    deriving (Show, Eq)

-- Note: no proper error reporting
newtype Parser a = Parser 
    { runParser :: String -> Maybe (String, a) }

instance Functor Parser where
    fmap f (Parser p) = 
        Parser $ \input -> do
          (input', x) <- p input
          Just (input', f x)

instance Applicative Parser where
    pure x = Parser $ \input -> Just (input, x)
    (Parser p1) <*> (Parser p2) = 
        Parser $ \input -> do
            (input', f) <- p1 input
            (input'', a) <- p2 input'
            Just (input'', f a)

instance Alternative Parser where
    empty = Parser $ \_ -> Nothing
    (Parser p1) <|> (Parser p2) = 
        Parser $ \input -> p1 input <|> p2 input

jsonNull :: Parser JSonValue
jsonNull = (\_ -> JSonNull) <$> stringP "null"

charP :: Char -> Parser Char 
charP x = Parser f
        where 
            f (y:ys)
                |  y == x = Just (ys, x)
                | otherwise =  Nothing
            f [] = Nothing
        
stringP :: String -> Parser String
stringP = sequenceA . map charP

jsonBool :: Parser JSonValue
jsonBool = f <$> (stringP "true" <|> stringP "false")
    where f "true"  = JSonBool True 
          f "false" = JSonBool False 
          --This should never happen
          f _       = undefined

spanP :: (Char -> Bool) -> Parser String
spanP f = 
  Parser $ \input -> 
    let (token, rest) = span f input
    in Just (rest, token)

notNull :: Parser [a] -> Parser [a]
notNull (Parser p) = 
    Parser $ \input -> do
        (input', xs) <- p input
        if null xs
            then Nothing 
            else Just (input', xs)

jsonNumber :: Parser JSonValue
jsonNumber =  f <$> notNull (spanP isDigit )
    where f ds = JSonNumber $ read ds

stringLiteral :: Parser String
stringLiteral = spanP (/= '"')

jsonString :: Parser JSonValue
jsonString = JSonString <$> (charP '"' *> stringLiteral <* charP '"')
            
jsonValue :: Parser JSonValue
jsonValue = jsonNull <|> jsonBool <|> jsonNumber <|> jsonString

ws :: Parser String
ws = spanP isSpace

sepBy :: Parser a -> Parser b -> Parser [b]
sepBy sep element = (:) <$> element <*> many (sep *> element)

jsonArray :: Parser JSonValue
jsonArray = JSonArray <$> (charP '[' *> ws *> 
                           elements
                           <* ws <* charP ']')
    where 
        elements = sepBy (ws *> charP ',' <*  ws) jsonValue

main :: IO ()
main = undefined