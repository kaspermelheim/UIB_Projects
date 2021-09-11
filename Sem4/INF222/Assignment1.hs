-- Assignment 1
-- 1.3
f :: Int -> Int -> Int
f x y = x + y

-- oppg. 1

-- 1
sum_squares :: Int -> [Int]
sum_squares 0 = []
sum_squares x = x^2 : sum_squares (x - 1)

sum_squares' :: Int -> [Int]
sum_squares' 0 = []
sum_squares' x = [x^2 | x <- [0..x]]

-- 2
-- find_indice x a = if x == a then True 
                --   else False

--find_indices (x:xs) a = if find_indice x a then (findIndex a (x:xs)) else find_indices xs a

find_indices :: (Num a1, Enum a1, Eq a2) => [a2] -> a2 -> [a1]
find_indices str ch = [ y | (x, y) <- zip str [0..], x == ch ]

-- 3
--mapFunc _ [] = []
--mapFunc func (x:xs) = map func x : mapFunc func xs

-- 4
data Expr = T | F | And Expr Expr | Or Expr Expr | Not Expr

eval :: Expr -> Expr
eval (And T T) = T
eval (And T F) = F
eval (And F T) = F
eval (Or T T) = F
eval (Or T F) = T
eval (Or F T) = T
eval (Or F F) = F
eval (Not T) = F
eval (Not F) = T

-- 5
isSorted :: [Int] -> Bool
isSorted [] = True
isSorted [x] = True
isSorted (x:y:xs) = if x > y then False
                    else if x < y then isSorted (y:xs)
                    else True

-- 6

find :: k -> [(k, v) ] -> Maybe v
find targetKey dict = undefined

names :: [( Int , String ) ]
names = [(0, "Bob"), (5, "Carol") ]

--find 1 names −− Returns: Nothing
--find 5 names −− Returns: Just "Carol"

-- 10

data Account = Admin String | User String [String] | Guest

-- 11
isAllowedAccess :: Account -> Bool
isAllowedAccess (User name perms) = if elem "write" perms then True else False
isAllowedAccess (Admin name) = True
