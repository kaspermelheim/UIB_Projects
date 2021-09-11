-- Kap 1.7
-- #1
{-
double x = x + x
double(double 2) = double(2 + 2) = double(4) = 4 + 4 = 8
-}
-- #2
{-
sum[] = 0 --kun et element, og det har sin egen sum
sum(x:xs) = x + sum xs = x + sum [] = x + 0 = x 
-}
-- #3
{-
product[] = 1
product(x:xs) = x * product xs

product[2,3,4] 
= 2 * product[3,4] 
= 2 * 3 * product[4] 
= 2 * 3 * 4 * product[] 
= 2 * 3 * 4 * 0 = 24
-}
-- #4
-- qsort with reversed list
qsortRev[] = []
qsortRev (x:xs) = qsortRev larger ++ [x] ++ qsortRev smaller
        where 
            larger = [a | a <- xs, a >= x] 
            smaller = [b | b <- xs, b < x]
-- #5
-- qsort original men uten <=
qsort[] = []
qsort (x:xs) = qsort smaller ++ [x] ++ qsort larger
        where 
            smaller = [a | a <- xs, a < x]
            larger = [b | b <- xs, b > x]
-- qsort[2,2,3,1,1] = [1,2,3] -- element med lik verdi i den gamle lista, vil kun dukke opp 1 gang i den nye sorterte lista. Duplikat blir fjernet

-- Kap 2.7
-- #2
{-
2^3*4 = (2^3)*4 = 32
2*3+4*5 = (2*3)+(4*5) = 26
2+3*4^5 = 2+(3*(4^5))
-}

-- #3
new = a `div` length xs
    where
        a = 10
        xs = [1,2,3,4,5]

-- #4

last1 [] = error "tom liste"
last1 [x] = x
last1 (x:xs) = last1 xs

last2 xs | xs == [] = error "tom liste"
         | length xs > 1  = last2 (tail xs)
         | length xs == 1 = head xs

        

-- #5

init1 :: [Integer] -> [Integer]
init1 [] = error "tom liste"
init1 [x] = []
init1 (x:xs) = x : init1 xs

init2 xs | xs == [] = error "tom liste"
         | length xs == 1 = []
         | otherwise = head xs : init2 (tail xs)

-- C #1
plu ::  [Integer] -> Integer -> [Integer]
plu xs n = map (\x -> x + n) xs 

-- C #2
pali :: Eq a => [a] -> Bool
pali [x] = False
pali [] = True
pali xs = if (head xs) /= (last xs) then False
                else pali (init(tail xs))
