--Ukesoppgave 7

--7.1
map1 :: (a -> b) -> [a ] -> [b ]
map1 f xs = [f x | x <- xs]

map2 :: (t -> a) -> [t] -> [a]
map2 f [ ] = [ ]
map2 f (x : xs) = f x : map2 f xs

filter1 :: (a -> Bool) -> [a] -> [a]
filter1 p xs = [x | x <- xs, p x]

filter2 :: (a -> Bool) -> [a] -> [a]
filter2 p [] = []
filter2 p (x : xs) | p x = x : filter2 p xs
                   | otherwise = filter2 p xs
--Ved å bruke filter og map kan man skrive listekomprehensjonen [f x | x <- xs, p x ] på denne måten: 
--map f (filter p lst)
--eks: map (+2) (filter even [1..15])

--7.4
foldr1 :: (a -> b -> b) -> b -> [a ] -> b
foldr1 f v [ ] = v
foldr1 f v (x : xs) = f x (foldr f v xs)

--dec2int [2,3,4,5] == 2345
dec2int :: [Int ] -> Int
dec2int = foldl (\x y -> 10 * x + y) 0

--7.5
{--
sumsqreven :: t
sumsqreven = compose [sum, map (^2), filter even ]

Denne er feil siden map og filter even returnerer en liste, mens sym har typen sum :: (Num a) => [a] -> a , og returnerer et element a,
og funksjonen vil derfor ikke fungere. --}

--7.9
--Altmap
altMap :: (a -> b) -> (a -> b) -> [a] -> [b]
altMap f g [] = []
altMap f g (x:[]) = [ f x ]
altMap f g (x:y:xs) = f x : g y : altMap f g xs

--8.5
data Expr = Val Int | Add Expr Expr

--Folde
folde :: (Int -> a) -> (a -> a -> a) -> Expr -> a
folde f g (Val x)   = f x
folde f g (Add x y) = g (folde f g x) (folde f g y)

--8.6
--Eval
eval :: Expr -> Int
eval x = folde id (+) x

--Size
size :: Expr -> Int
size x = folde (\_ -> 1) (+) x

--B
--Innfiks
infiks :: Expr -> String
infiks s = inn s

inn :: Expr -> String
inn (Add x y) = innP x ++ " + " ++ innP y
inn expr = innP expr

innP :: Expr -> String
innP (Val n) = show n
innP (Add x y) = "(" ++ innP x ++ " + " ++ innP y ++ ")"

prefiks :: Expr -> String
prefiks s = pre s

pre :: Expr -> String
pre (Add x y) = " + " ++ preP x ++ " " ++ preP y
pre expr = preP expr

preP :: Expr -> String
preP (Val n) = show n
preP (Add x y) = "+ " ++ preP x ++ " " ++ preP y

postfiks :: Expr -> String
postfiks s = post s

post :: Expr -> String
post (Add x y) = postP x ++ " " ++ postP y ++ " +"
post expr = postP expr

postP :: Expr -> String
postP (Val n) = show n
postP (Add x y) = postP x ++ " " ++ postP y ++ " +"

