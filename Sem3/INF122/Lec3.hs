import Data.Char
mind x [] = []
mind x (y:ys) = if (x>y) 
    then (y:mind x ys) 
    else (mind x ys)

str x [] = []
str x (y:ys) = if (x>y) then (str x ys) else (y:str x ys)

{-Quicksort alle element i en liste -}
qs [] = []
qs (x:xs) = qs (mind x xs) ++ [x] ++ qs (str x xs) 

opp = toUpper 'a'

