fill ls x n = take n (ls ++ repeat x)

fillf ls x n = reverse (take n (reverse ls ++ repeat x))

b2d bt = sum [ w*b | (w,b) <- zip (reverse bt) (iterate (2*) 1) ]

{-
foldl :: (b -> a -> b) -> b -> [a] -> Bool
[1,0,1,1]
2 * (2 * ((2*1) + 0) + 1) + 1
-}

fb2d :: [Int] -> Int
fb2d = foldl (\a h -> 2*a + h) 0

debi 0 = []
debi dt = (dt `mod` 2) : debi(dt `div` 2)

say = putStrLn "Hello"
fun = "Hei"

m = do
    linje <- getLine
    if(null linje) then return ()
    else do
        putStrLn (rev linje)
        m
        
rev :: String -> String
rev = unwords . map reverse . words