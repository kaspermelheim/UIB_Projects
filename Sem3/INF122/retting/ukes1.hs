--B
-- 1.4

let
    qsort :: Ord a => [a] -> [a]
    qsort [] = []
    qsort (x:xs) = qsort larger ++ [x] ++ qsort smaller
                 where smaller = [y | y <- xs, y <= x]
                       larger = [y | y <- xs, y > x]
  
{-qsort "Golden Thumb"
"uonmlhedbTG "
qsort [3,5,1,0,-2,9]
[9,5,3,1,0,-2]
qsort "Good morning"
"rooonnmigdG " -}

----------------------------------------------------------------

-- 1.5

let
  qsort :: Ord a => [a] -> [a]
  qsort [] = []
  qsort (x:xs) = qsort smaller ++ [x] ++ qsort larger
                 where smaller = [y | y <- xs, y < x]
                       larger = [y | y <- xs, y > x]
  
qsort "Good morning"
" Gdgimnor"
qsort [2,2,3,1,1]
[1,2,3]
qsort "Good morning"
" Gdgimnor"

-------------------------------------------------------------------

-- 2.4

let 
 last' :: [a] -> a
 last' xs = head $ reverse 

last' [1..20]
20


----------------------------------------------------------------------


-- 2.5

let 
    init' :: [a] -> [a]
    init' xs = take (length xs - 1) xs
 
init' [1..20]
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]


---------------------------------------------------------------------

-- C

-- 1

let
    replace [] _ = []
    replace (_:xs) (0,a) = a:xs
    replace (x:xs) (n,a) =
        if n < 0
            then (x:xs)
            else x: replace xs (n+x,a)

------------------------------------------------------------------------


-- 2

isPalindrome :: String -> Bool
isPalindrome w = w == reverse w 
