--Ukesoppgave 3
--A
--4.5
(&&) :: Bool -> Bool -> Bool
a && b = if a == True then
           if b == True then True
           else False
         else False

--4.7
mult :: Int -> Int -> Int -> Int
--mult x y z = x*y*z
mult = \x -> \y -> \z -> x*y*z

--B
--5.6
factors :: Int -> [Int]
factors a = [x | x <- [1..a], a `mod` x == 0]

perfects :: Int -> [Int]
perfects a = [x | x <- [1..a], (sum (factors x)) - x  == x]

--5.7

fun :: [a] -> [b] -> [(a, b)]
fun xs ys = concat [map (\y -> (x, y)) ys | x<-xs]

--C
rem1 :: Eq a => [a] -> a -> [a]
rem1 [] a = []
rem1 (x:xs) a = if x == a then xs
                else x : rem1 xs a

--D
diff :: Eq a => [a] -> [a] -> [a]
diff (x:xs) [] = (x:xs)
diff xs (y:ys) = diff (rem1 xs y) ys

--E
luhnDouble :: Int -> Int
luhnDouble x = let x' = 2 * x in if x' > 9 then x' -9 else x'
