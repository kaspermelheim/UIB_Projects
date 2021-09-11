-- Høst 2019
-- Oppg. 1

-- 1.1
-- filter even (map (*2) [1..5]) == [2,4,6,8,10]

-- 1.2
-- take 5 nats,1,2,3
nats :: [Integer]
nats = 0:1:tail nats -- gir [0,1,1,1,1]

nats1 :: [Integer]
nats1 = 0:map (+1) nats1 -- gir [0,1,2,3,4]

nats2 :: [Integer]
nats2 = 0:tail nats2 -- gir [0 og programmet henger siden tail nats2 ikke er definert

nats3 :: [Integer]
nats3 = map (+1) [0..] -- gir [1,2,3,4,5]

-- 1.3
-- concat ["ab", "cd", "", "efg"]
concat1 :: [a] -> [a]
concat1 xss = [x | x<-xss] -- gir ["ab", "cd", "", "efg"]

concat2 :: [[a]] -> [a]
concat2 xss = [x | xs<-xss, x<-xs] -- gir "abcdefg"

concat3 :: [[a]] -> [a]
concat3 xss = concat3 (tail xss) -- gir " og programmet henger siden starten av lista mangler

concat4 :: [[a]] -> [[a] -> [a]]
concat4 xss = map (++) xss -- gir feilmelding

-- 1.4
apply :: (t1 -> t2) -> t1 -> t2
apply f x = f x

-- Oppg. 2
-- 2.1
-- row [[1,2],[3,4]] 2 = [3,4]
row::[[Int]] -> Int -> [Int]
row m r = m!!(r-1) 

-- 2.2
--  col [[1,2],[3,4]] 1 = [1,3]
col::[[Int]] -> Int -> [Int]
col m r = map (!!(r-1)) m

-- 2.3
-- cols [[1,2],[3,4]] = [[1,3],[2,4]]
cols::[[Int]] -> [[Int]]
cols m = map (\x -> col m x) [1..(length m)]

-- 2.4
-- [[1,2],[3,4]] [[3,4],[5,6]] = [[13,16],[29,36]]
mult::[[Int]]->[[Int]]->[[Int]]
mult ma mb = [map (multrc (row ma x)) (cols mb) | x <- [1..length ma]]

multrc :: Num a => [a] -> [a] -> a
multrc r c = sum [x*y | (x,y) <- zip r c]

-- Oppg. 3
