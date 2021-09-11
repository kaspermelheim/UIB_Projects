-- Kasper Melheim, INF122, gruppe 2
module Oblig1 where
import Data.Char
--Henter ulike innebygde funksjoner fra Data.Char

--Oppg.1
--Jeg har valgt å løse oppgaven ved å lage separate parse funksjoner for de ulike datatypene, og kaller på de i den rekkefølgen jeg ønsker

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

--Tokenize, gjenbruk av kode fra ukesoppg. 5. Funksjon som sjekker hvilket tegn vi har fått som input, og plasserer den i rett katevalri
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

--parse funksjon som parser faktorer (int og string)
parseNumOrWord :: [String] -> (Ast, [String])
parseNumOrWord [] = error "unexpected end of input"
parseNumOrWord (x : xs)
  | isNumToken x = (Num (read x), xs)
  | isWordToken x = (Word x, xs)
  | otherwise = error ("unrecognized token " ++ show x)

--parse funksjon som parser multiplikasjon (Mult)
parseMult :: [String] -> (Ast, [String])
parseMult xs
  =  let (y1, xs1) = parseNumOrWord xs
     in  val y1 xs1
     
  where val o ("*" : xs2)
          = let (y2, xs3) = parseNumOrWord xs2
            in val (Mult o y2) xs3
        val o end = (o, end)

--parse funksjon som parser addisjon (Plus)
parsePlus :: [String] -> (Ast, [String])
parsePlus xs
  =  let (y1, xs1) = parseMult xs
     in  val y1 xs1

  where val o ("+" : xs2)
          = let (y2, xs3) = parseMult xs2
            in val (Plus o y2) xs3
        val o end = (o, end)

--parse funksjon som parser subtraksjon (Minus)
parseMinus :: [String] -> (Ast, [String])
parseMinus xs
  =  let (y1, xs1) = parsePlus xs
     in  val y1 xs1

  where val o ("-" : xs2)
          = let (y2, xs3) = parsePlus xs2
            in val (Minus o y2) xs3
        val o end = (o, end)

--Wrapper funksjon parse rundt parseMinus, som kaller på de andre funksjonene. Gir error dersom ulovlig
parse :: String -> Ast
parse x =

  case parseMinus (tokenize x) of
    (i, []) -> i
    (_, j : _) -> error ("unexpected token " ++ (show j))

--Oppg.2
vis :: Ast -> IO ()
vis ast = putStr (vis' ast)

indent :: Int -> [Char]
indent n = concat $ take n (repeat "   ")

vis' :: Ast -> String
vis' ast = vissH ast 0

vissH :: Ast -> Int -> String
vissH (Mult a a') n = indent n ++ "Mult"  ++ "\n" ++ vissH a (n+1) ++ vissH a' (n+1)
vissH (Plus a a' ) n = indent n ++ "Plus"   ++ "\n" ++ vissH a (n+1) ++ vissH a' (n+1)
vissH (Minus a a' ) n = indent n ++ "Minus"   ++ "\n" ++ vissH a (n+1) ++ vissH a' (n+1)
vissH (Num i    ) n = indent n ++ "Num " ++ show i ++ "\n"
vissH (Word i    ) n = indent n ++ "Word " ++ i ++ "\n"

--Oppg.3
eval :: Ast -> String
eval (Num n) = show n
eval (Plus a b) = eval a ++ eval b
eval (Mult (Num a) (Word b)) = duplicate b a
eval (Minus a b) = diff (eval a) (eval b)
eval (Word a) = a

duplicate :: String -> Int -> String
duplicate str n = concat $ replicate n str

diff :: Eq a => [a] -> [a] -> [a]
diff (x:xs) [] = (x:xs)
diff xs (y:ys) = diff (remove xs y) ys


remove :: Eq a => [a] -> a -> [a]
remove [] _ = []
remove (x:xs) y
     | x == y     = xs
     | otherwise  = x : remove xs y