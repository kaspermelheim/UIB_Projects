module Day2Part1 where

-- Operators

foo :: Int -> Int -> Int
--foo x y = x
x `foo` y = x

(%) :: Int -> Int -> Int 
x % y = mod x y 

-- Partial application

add :: Int -> Int -> Int
add x y = x + y

--mult :: Int -> Int -> Int -> Int
--mult x y z = x * y * z

-- Lambda functions

double :: Int -> Int 
-- double x = x + x
double = \x -> x + x

mult :: Int -> Int -> Int 
-- mult x y = x * y
-- mult = \x -> \y -> x * y
mult = \x y -> x * y

first :: (a, b) -> a
-- first (x, _) = x
first = \(x, _) -> x

dropSmallerThanThree :: [Int] -> [Int]
dropSmallerThanThree xs = filter (< 3) xs
--   where
    -- lessThanThree :: Int -> Bool
    -- lessThanThree x = x < 3


