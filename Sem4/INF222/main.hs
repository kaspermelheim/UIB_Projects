
doubleAll :: [Int] -> [Int]
doubleAll [] = []
doubleAll (x:xs) = x * 2 : doubleAll xs

double :: Int -> Int 
double x = x * 2

square :: Int -> Int 
square x = x ^ 2

doSomethingToAll :: (Int -> Int) -> [Int] -> [Int]
doSomethingToAll f [] = []
doSomethingToAll f (x:xs) = f x : doSomethingToAll f xs

filter2 :: (Int -> Bool) -> [Int] -> [Int]
filter2 f (x:xs) = if f x then x : filter2 f xs
                   else filter2 f xs

any :: (a -> Bool) -> [a] -> Bool 
any f [] = False 
any f (x:xs) = f