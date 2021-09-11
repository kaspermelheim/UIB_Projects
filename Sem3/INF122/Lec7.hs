rev :: [a] -> [a] -> [a]
rev [] l2 = l2
rev (x:xs) l2 = rev xs (x:l2)

app :: [a] -> [a] -> [a]
app l1 l2 = if null(l1) then l2 else (head l1) : (app (tail l1) l2)

qs [] = []
--qs (x:xs) = qs (mindre xs x) ++ [x] ++ qs(stoerre xs x)

--summererer kvadratet av alle tall opp til x
--f 1 = 1
--f 2 = 5
--f 3 = 14
f :: (Num a, Enum a) => a -> a
f x = sum [ n*n | n <- [1..x] ]