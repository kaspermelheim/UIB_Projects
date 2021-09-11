import Data.List (intersperse)

--Uke 8
--Oppg. 1
--A
--Sjekker om alle element i lista er true med rekursjon
al :: [Bool] -> Bool
al [] = True
al (x:xs) = if x == False then False
            else al xs

--B
--Sjekker om alle element i lista er true med innebygd funksjon "all"
all1 :: [Bool] -> Bool
all1 xs = all (== True) xs

--C
--Sjekker om alle element i lista er true med foldl
al' :: [Bool] -> Bool
al' xs = foldl (\acc x -> acc && x) True xs

--D
--Sjekker om alle element i lista er true med foldr
al'' :: [Bool] -> Bool
al'' xs = foldr (\x acc -> acc && x) True xs

--Oppg. 2
ala :: (Bool -> Bool -> Bool) -> Bool -> [Bool] -> Bool
ala _ p [] = p
ala f p xs = foldl f p xs

--Oppg. 3
--trekant :: Int -> IO ()
trekant :: Int -> IO()
trekant lvl = putStr $ trekanthjelper lvl

trekanthjelper lvl = concat [concat (replicate i "* ") ++ "\n" | i <- [1..lvl]]

--Oppg. 4

trekant' :: Int -> IO()
trekant' = putStr . trekanthjelper
    where trekanthjelper lvl = concat [replicate (lvl -1) ' ' ++ concat (replicate i "* ") ++ "\n" | i <- [1..lvl] ]

