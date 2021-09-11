-- Kap 3
-- #B: 3.3
second :: [a] -> a
second xs = head (tail xs)

swap :: (a,b) -> (b,a)
swap (x,y) = (y,x)

pair :: a -> b -> (a,b)
pair x y = (x,y)

double :: Num a => a -> a
double x = x*2

palindrome :: Eq a => [a] -> Bool
palindrome xs = reverse xs == xs

twice :: (t -> t) -> t -> t
twice f x = f (f x)

-- #C:
{-
False :: Bool
5 + 8 :: Num a => a
(+) 2 :: Num a => a -> a
(+2) :: Num a => a -> a
(2+) :: Num a => a -> a
(["foo", "bar"], 'a') :: ([[Char]], Char)
[(True, []), (False, [['a']])] :: [(Bool, [[Char]])]
\x y -> y !! x :: Int -> [a] -> a
[ take, drop, \x y -> ( y !! x ) ] :: {-Gir error-}
[ take, drop, \x y -> [ y !! x ] ] :: [Int -> [a] -> [a]]
-}

-- #D:
{-Alle funksjonene er ekvivalent unntatt foo5, der b og a har byttet plass i typen-}
foo1 :: a -> b -> (a,b)
foo1 x y = (x, y)

foo2 :: a -> b -> (a, b)
foo2 x = \y -> (x, y)

foo3 :: a -> b -> (a, b)
foo3 = \x y -> (x, y)

foo4 :: a -> b -> (a, b)
foo4 = \x -> \y -> (x, y)

foo5 :: b -> a -> (a, b)
foo5 = \x -> \y -> (y,x)

foo6 :: a -> b -> (a, b)
foo6 = \y -> \x -> (y,x)

-- #E:

f1 :: a -> (a,a)
f1 x = (x,x)

f2 :: (a,b) -> a
f2 (x,y) = x

f3 :: (a,b) -> b
f3 (a,b) = b

f4 :: a -> b -> a
f4 x y = x

f5 :: a -> b -> b 
f5 x y = y

-- #F:
f :: Int -> Int -> Int
f x y = x

g :: (Int, Int) -> Int
g (x,y) = x



