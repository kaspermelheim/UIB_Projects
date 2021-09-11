-- Høst 2018
-- Oppg. 1
-- 1.1
-- mengde [1,2,3] = True 
-- mengde "abcb" = False
mengde :: Eq t => [t] -> Bool
mengde list = case list of
    []     -> True
    (x:xs) -> x `notElem` xs && mengde xs

-- 1.2
rep :: Eq t => [t]->[t]
rep = foldl (\check x -> if x `elem` check
                        then check
                        else check ++ [x]) []

-- 1.3
del :: Eq t => [t]->[t]->Bool
del [] _ = True
del (x:xs) ys = elem x ys && del xs ys

-- 1.4
eq::Eq t => [t]->[t]->Bool
eq x y = del x y && del y x

-- 1.5
eqG::(t->t->Bool)->[t]->[t]->Bool
eqG pr xs ys = delG pr xs ys && delG pr ys xs

delG :: (t1 -> t2 -> Bool) -> [t1] -> [t2] -> Bool
delG pr [] _ = True
delG pr (x:xs) ys = or [ pr x y | y <- ys] && delG pr xs ys

-- 1.6

-- Oppg. 2
-- 2.1
kL = [("a","c"),("b","a"),("c","b"),("d","c"),("d","e")]

snuK::[(t,t)]->[(t,t)]
snuK [] = []
snuK ((x,y):rest) = (y,x) : snuK rest

snuK1 :: [(b, a)] -> [(a, b)]
snuK1 kl = [(y,x) | (x,y) <- kl]

-- 2.2

-- Oppg. 3
main = do
    putStr "liste / CR: "
    cc <- getLine
    let c = words cc
    if null c then return ()
    else if (head c == "L") then do
        inh <- readFile (head (tail c))
        vis (words inh)
        main
    else do
        vis c
        main

vis x = if (mengde x) then skriv (ps x)
        else putStrLn "Listen er ikke en mengde."

skriv xs = mapM_ putStrLn (map show xs)

ps xs = pl (rep xs)
pl :: [a] -> [[a]]
pl [] = [[]]
pl (x:xs) = [ s | r <- pl xs, s <- [x:r,r] ]

-- andre ligningen for pl kan bli annerledes, f.eks.:
