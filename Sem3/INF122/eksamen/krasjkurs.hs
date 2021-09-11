findElem :: (Foldable t, Eq a) => t a -> a -> Bool
findElem xs a = if a `elem` xs then True
                else False

findElem2 :: Eq t => [t] -> t -> Bool
findElem2 (x:xs) a = if x == a then True else findElem2 xs a

fib :: (Eq a, Num a, Num p) => a -> p
fib 0 = 0
fib 1 = 1
fib x = fib (x-1) + fib (x-2) 

erstatt :: String -> Char -> String
erstatt ss c = map (\x -> if x == c then 'x' else x) ss
