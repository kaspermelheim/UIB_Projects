fu x y = x + y --function fu

g x = -1 --function g

fib1 1 = 1
fib1 n = fib1 (n-1) + fib1 (n-2) -- fibonachi

sm1 xs = if (null xs) then 0 else (head xs) + (sm1 (tail xs))

append [] ys = ys
append (x:xs) ys = x : append xs ys --Legger til liste1 xs og liste2 ys til en liste

sm [] = 0
sm (n:ns) = n + sm ns -- summere alt i en liste, kan også gjøres med innebygd "sum"


rev [] = [] --reversere en liste
rev (x:xs) = (rev xs) ++ [x] --reversre liste, innebygd "reverse"

{-
ins [2,4,3,5] == [2,4,3,5] --flytter listens første element til pos med større påfølgende elemnt
ins [6,2,3,5] == [2,3,5,6]
-}

ins [] = []
ins [x] = [x]
ins (x:y:xs) = if (x <= y) then x:y:xs else y: ins(x:xs)

inss [] = []
inss (x:xs) = ins(x: (inss xs))

init [1,2,3,4] = [1,2,3] -- dropper siste element i liste

{- Dropper og tar elemnt fra liste}
take 2 [1,2,3,4,5] = [1,2]
take 5 [1,2,3,4,5,6] = [1,2,3,4,5]
drop 3 [1,2,3,4,5] = [4,5]

length [1,2,3] = 3 --gir lengde på liste
-}

product [1,2,3,4] = 24 --produkt av tallene i liste
sum [1,2,3,4] = 10 --sum av tallene i liste

last [x] = x --henter siste element i liste
last [1,2,3,4] = 4
--last (x:xs) = last xs

ones = 1:ones --uendelig liste av 1
take 5 ones = [1,1,1,1,1] --henter 5 1ere


