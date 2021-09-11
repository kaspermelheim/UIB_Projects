import Data.Char
-- Høst 2017
-- Oppg. 1
-- 1.1
-- harEl (==3) [1,1,2,3,2] = True
-- harEl (<3) [1,1,2,3,2] = True
harEl :: (t -> Bool) -> [t] -> Bool
harEl pr [] = False
harEl pr (y:ys) = if (pr y) then True else harEl pr ys

-- 1.2
-- el ((=='a').fst) [('a',2),('a',3),('a',4)] = ('a',3)
-- el ((>3).snd) [(’b’,2),(’a’,3),(’a’,4)] = (’a’,4).
el::(t->Bool)->[t]->t
el pr (x:xs) = if (pr x) then x else el pr xs

--1.3
-- gRep (<’d’) ’z’ ‘‘abcd’’ = ‘‘zzzd’’
-- gRep (==’a’) ’x’ ‘‘abcbcac’’ = ‘‘xbcbcxc’’.
gRep :: (t->Bool) -> t -> [t] -> [t]
gRep pr y = map (\x -> if (pr x) then y else x)

-- 1.4
data BT = B Int | N BT Int BT
-- a)
-- elt (N (B 1) 2 (B 0)) 2 = True
-- elt (B 1) 2 = False
elt :: BT -> Int -> Bool 
elt (B x) y = x == y
elt (N l v r) y = v == y || elt l y || elt r y

-- b)
--toL :: BT -> [Int]
--toL (B x) =  [x] toL (N l v r) = (toL l) ++ [v] ++ (toL r)

-- c)
dup :: [Int] -> Bool 
dup tr = dupL tr

dupL :: Eq a => [a] -> Bool
dupL [] = False
dupL (x:xs) = elem x xs || dupL xs

-- Oppg. 2
-- 2.1
kL = [("a","b"),("a","c"),("b","d"),("c","b"),("d","c"),("d","e")]

-- naboL kL = [(a, [b, c]),(b, [d]),(c, [b]),(d, [c, e]),(e, [])]
naboL :: (Eq a, Eq t) => [(t, a)] -> [(t, [a])]
naboL xs = foldr addk [] xs
addk (a,b) nL = if (harEl ((== a).fst) nL) then
    let (x,y) = el ((== a).fst) nL in gRep (==(x,y)) (x,b:y) nL
    else (a,[b]):nL

-- 2.2

length' :: (Num b) => [a] -> b 
length' [] = 0 
length' xs = sum [1 | _ <- xs]

kantDup :: [(t,[t])] -> [(t,t)]
kantDup [] = []
kantDup ((x,y:ys) : xs) = if length' (y:ys) > 1 then kantL ((x,y:ys):xs) else (x, y) : kantDup xs

kantL :: [(t, [t])] -> [(t, t)]
kantL ((x,y:ys) : xs) = (x, y) : kantDup ((x,ys):xs)

-- 2.3
-- a
-- naboer kL "a" = ["b","c"]
-- naboer kL "e" = []
naboer :: (Eq t, Eq t) => [(t,[t])] -> t -> [t]
naboer [] _ = []
naboer ((x,y:ys) : xs) a = if x == a then 
                                if length' (y:ys) == 0 then []
                                else if length' (y:ys) == 1 then [y]
                                else if length' (y:ys) > 1 then y : ys
                                else [y]
                            else naboer xs a
-- b
cyc :: (Eq t, Eq t) => [(t,[t])] -> t -> [t]
cyc [] _ = []
cyc ((x,y:ys) : xs) a = if x == a then
                            if length' (y:ys) == 0 then []
                            else x : cyc xs y
                        else x : cyc xs a

main :: IO ()
main = run []

run :: [(Int,Int)] -> IO ()
run gr = do
    print (show gr)
    input <- getLine
    let index = words input
    case index of
        ("q":_) -> return ()
        ("s":_) -> run gr
        ("g":_) -> do
            run gr
        ("k":x:y:_) -> do
            let x = read (head (tail index)) :: Int
                y = read (head (tail (tail index))) :: Int
            if (x,y) `notElem` gr then run ((x,y):gr)
            else run gr
        ("f":x:y:_) -> do
            let x = read (head (tail index)) :: Int
                y = read (head (tail (tail index))) :: Int
            if (x,y) `elem` gr then run (filter (/=(x,y)) gr)
            else run gr
        _ -> do
            putStrLn "Ugylding input."
            run gr