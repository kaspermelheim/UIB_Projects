-- 284
-- INF122 Eksamen

-- Oppg. 1

-- 1.1 
-- foldl (-) 0 [2,4,6]
-- Denne funksjonen "folder" alle element i listen fra venstre (l for left) til tallet 0 med operatoren "-"
-- (0 - 2) - 4) - 6)    | Steps:    0 - 2 = -2  |  -2 -4 = -6  | -6 - 6 = -12 
-- Svaret: -12

-- 1.2
-- foldr (-) 0 [2,4,6]
-- Denne funksjonen "folder" alle element i listen fra hlyre (r for right) til tallet 0 med operatoren "-"
-- (2 - (4 - (6 - 0)    | Steps:    6 - 0 = 6   |   4 - 6 = -2  |  2 - (-2) = 4
-- Svaret: 4

-- Oppg. 2

-- 2.1
funk ::  Eq a => [a] -> Bool
funk [] = True
funk [a] = True
funk (a:b:c:xs) = if a == c then False else funk (c:xs) 
          
-- 2.2
avb::Eq a => [a]->[a]->[a]
avb str ls = if funk ls == False then str
             else ls

-- 2.3
fle::Eq a => [a]->[a]->[a]
fle xs [] = xs
fle [] ys = ys
fle (x : xs) (y : ys) = x : y : fle xs ys

-- 2.4
bin ::  (Int->Int->Int) -> String -> String -> String
bin a x y = show (a (read x) (read y))

-- 2.5
umin::String->String
umin x = show (- (read x))

-- Oppg. 3

-- Kommer til å klage på vanskelighetsgraden på denne oppgaven, og dens vekt på poengscoren til denne eksamen.

-- 3.1
-- Bør få litt uttelling her, har ikke klart å løst den 100%
eva::String->(String,String)
eva ('*' : ls) = (show r, lss)
    where
        (a, b) = eva ls
        (c, lss) = eva b
        r = (read a :: Int) * (read c :: Int)

eva (' ' : ls) = eva ls

eva (l:ls) = (l:[], ls)

-- 3.2
evg::  String  -> (String->String->String)-> (String->String->String)-> (String->String)-> (String->String) -> (String,String)
evg = undefined

-- 3.3

-- 3.4
str :: String
str = undefined

-- Oppg. 4

-- Vil skrive en lambda funksjon som gir samme output some f
f :: (Eq p, Num p) => p -> p -> p
f x 0 = 0
f x y = (x * y) + f x (y-1)

-- Løst med lambda:

g :: Integer -> Integer -> Integer
g = (\a -> \b -> if b == 0 then 0 else a * b + (g a (b-1))) 

-- Oppg. 5

-- Gi typeavledning av: \x -> x (\y ->\z -> y z)
test :: (((t1 -> t2) -> t1 -> t2) -> t3) -> t3
test = \x -> x (\y -> \z -> y z)
-- Typeavledning på delType = (\y ->\z -> y z) gir:

-- Ø              |   \y -> \x -> y x  :: a   | Ø
-- y :: b         |   \x -> y x :: c          | a = b -> c
-- y :: b, x :: d |   y x :: e                | a = b -> c, c = d -> e
-- y :: b, x :: d |   y :: f -> e             | a = b -> c, c = d -> e
-- y :: b, x :: d |   x :: f                  | a = b -> c, c = d -> e

-- Unifikasjon:

-- a = b -> c, c = d -> e, b = f -> e, f = d
-- a = b -> c, c = d -> e, b = d -> e, f = d
-- a = (d -> e) -> (d -> e), c = d -> e, b = d -> e, f = d

-- typen til denne deltypen er :: (d -> e) -> d -> e

-- Oppg. 6

{- Gitt:

(++) :: [a] -> [a]
[] ++ ys = ys
(x:xs) ++ ys = x : (xs++ys)

og:

filter :: (a -> Bool) -> [a] -> [a]
filter p [] = []
filter p (x:xs) = if (p x) then x:(filter p xs) else (filter p xs)

vil vise at for alle endelige lister xs og ys gjelder:

filter p (xs ++ ys) = filter p xs ++ filter p ys

1. Base case for induksjon: filter p [] = []

2. Induksjonshypotese: 

-}
