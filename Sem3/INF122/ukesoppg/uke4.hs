--Ukesoppgave 4
import Data.List
--A
--fjern med rekursjon
fjern :: String -> Char -> String
fjern [] a = []
fjern (x:xs) a = if x == a then fjern xs a
                 else x : fjern xs a

--fjern med listekomprehensjon
fjern1 :: String -> Char -> String
fjern1 [] a = []
fjern1 xs a = [ x | x <- xs, x /= a ]

--B
--tegnpos
--tegnpos med listekomprehensjon
tegnpos :: Char -> String -> [Int]
tegnpos a [] = []
tegnpos a xs = [ y | (x, y) <- zip xs [0..], x == a ]

--tegnpos med rekursjon
inc :: (Eq t, Num a) => [t] -> t -> a -> [a]
inc [] y n = []
inc (x:xs) y n = if y==x then n : inc xs y (n+1) else inc xs y (n+1)

tegnpos1 :: Char -> String -> [Int]
tegnpos1 x [] = []
tegnpos1 x ys = inc ys x 0

--C
inToList :: Int -> [Int]
inToList 0 = []
inToList a = inToList (a `div` 10) ++ [a `mod` 10]

--D #a
settSammen :: [String] -> String
settSammen xs = tail (settSammenHjelper xs) where
    settSammenHjelper [] = []
    settSammenHjelper (x:xs) = ' ' : x ++ settSammenHjelper xs

--D #b
delStrengen :: String -> [String]
delStrengen [] = []
delStrengen xs = let
    xs' = dropWhile (==' ') xs
    word = takeWhile (/=' ') xs'
    rest = dropWhile (/=' ') xs' in
        word : delStrengen rest

--D #c
gDelStrengen :: String -> String -> [String]
gDelStrengen [] _ = []
gDelStrengen xs as = let
    inAs x = elem x as
    notInAs x = not (inAs x)
    xs' = dropWhile (inAs) xs
    word = takeWhile (notInAs) xs'
    rest = dropWhile (notInAs) xs' in
        word : gDelStrengen rest as

dropWhile' :: (a -> Bool) -> [a] -> [a]
dropWhile' p [] = []
dropWhile' p (x:xs) = if p x then x : takeWhile' p xs else xs

takeWhile' :: (a -> Bool) -> [a] -> [a]
takeWhile' _ [] = []
takeWhile' p (x:xs) = if p x then x : takeWhile' p xs else []