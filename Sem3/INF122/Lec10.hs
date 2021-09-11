import Data.Char

tokenize :: Eq a => [a] -> [a] -> [a] -> [[a]]
tokenize [] t s = []
tokenize (x:xs) t s 
    | elem x t = [x] : tokenize xs t s 
    | elem x s = tokenize xs t s 
    | otherwise = (takeWhile (notin (t++s)) (x:xs)) : tokenize (dropWhile (notin (t++s)) (x:xs)) t s 
    
notin :: (Foldable t, Eq a) => t a -> a -> Bool
notin xs = \x -> not(elem x xs)

tokens :: [Char] -> [[Char]]
tokens xs = tokenize xs "*+" " "

data Ast = A Ast Ast | M Ast Ast | V Int deriving (Show)

--parseE :: [String] -> (Ast, [String])



onlyDigits xs = all isDigit xs

--parse :: [Char] -> a
--parse xs = fst(parseE (tokens xs))

ev :: Ast -> Int
ev (V x) = x
ev (A a b) = (ev a) + (ev b)
ev (M a b) = (ev a) * (ev b)

innf :: Ast -> String
innf (V x) = show x
innf (A a b) = "(" ++ (innf a) ++ "+" ++ (innf b) ++ ")"
innf (M a b) = "(" ++ (innf a) ++ "*" ++ (innf b) ++ ")"