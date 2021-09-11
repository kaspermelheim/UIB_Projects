newtype Nat = N Int

type Par n v = (n,v)
type Ordbok n v = [ Par n v ]

find :: Eq n => n -> (Ordbok n v ) -> v
find k obk = head [ v | (n,v) <- obk, n == k]

--data Direction = Ne | Se | Sw | Nw deriving (Eq, Ord, Show, Read)

{-data Dir = Ne | Nw | Se | Sw 

instance Show Dir where
    show Ne = "north east"
    show Nw = "north west"
    show Se = "south east"
    show Sw = "south west"

myshow :: Dir -> [Char]
myshow Se = "south east"
myshow x = show x
-}
data Fig = Circ Float | Rek Float Float deriving (Show,Eq,Read)


kvad :: Float -> Fig
kvad n = Rek n n

data Ret = Ve | Ho | Op | Ne deriving (Eq, Ord, Show, Read)

mv :: (Num a1, Num a2) => (a1, a2) -> Ret -> (a1, a2)
mv (x,y) Ve = (x-1,y)
mv (x,y) Ho = (x+1,y)
mv (x,y) Op = (x,y+1)
mv (x,y) Ne = (x,y-1)

mvs :: (Num a1, Num a2) => (a1, a2) -> [Ret] -> (a1, a2)
mvs p [] = p
mvs p (r:rs) = mvs (mv p r) rs 

--Leaf x er bladnode uten barn
--Emp er tomt tre
--Node x y z har y i roten med x i venstre og z i høyre subtre
data Tre = Leaf Int | Node Tre Int Tre | Emp deriving (Show)

list :: Tre -> [Int]
list (Leaf y) = [y]
list (Node l y r) = list l ++ [y] ++ list r

insert :: Int -> Tre -> Tre
insert x Emp = Leaf x
insert x (Leaf y) = if x<y then Node (Leaf x) y Emp
                    else Node Emp y (Leaf x)
insert x (Node l y r) = if x<y then Node (insert x l) y r 
                        else Node l y (insert x r)

inss :: [Int] -> Tre -> Tre
inss [] t = t
inss (x:xs) t = inss xs (insert x t)



