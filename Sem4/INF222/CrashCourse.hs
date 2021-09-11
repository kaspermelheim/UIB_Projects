-- Common types

import Data.Char (toUpper, isAlpha)

-- Int

one :: Int 
one = 1

three :: Int 
three = one + 2

successor :: Int -> Int 
successor x = x + 1

predecessor :: Int -> Int
predecessor x = x - 1

one' :: Int 
one' = div 3 2

-- Float

twoPointThree :: Float 
twoPointThree = 2.4

onePointTwo :: Float 
onePointTwo = twoPointThree / 2

-- Bool

haskellIsFun :: Bool 
haskellIsFun = True 

pizzaToday :: Bool
pizzaToday = False 

-- Tuples

intBool :: (Int, Bool)
intBool = (5, True)

swap :: (Int, Bool) -> (Bool, Int)
swap (i, b) = (b, i)

first :: (Int, Bool) -> Int 
first (i, _) = i

second ::(Int, Bool) -> Bool
second (_, b) = b

-- List

data MyList = Empty | Prepend Int MyList

myList1 :: MyList
myList1 = Prepend 1 (Prepend 2 Empty)

list1 :: [Int]
list1 = [1,2,3]

myHead :: [Int] -> Int
myHead (x:xs) = x
myHead [] = error "Head of empty list"

myTail :: [Int] -> [Int]
myTail (x:xs) = xs
myTail [] = error "tail of empty list"

-- Char

charA :: Char 
charA = 'a'

charB :: Char
charB = 'b'

upperB :: Char
upperB = toUpper charB

-- String / [Char]

abString :: String 
abString = "ab"

abListOfChar :: [Char]
abListOfChar = ['a', 'b']

helloWorld :: String 
helloWorld = "Hello" ++ " world!"

alphabet :: String 
alphabet = ['a' .. 'z']

oneToTen :: [Int]
oneToTen = [1 .. 10]

-- Tasks

-- Abs val of an int
absolute :: Int -> Int
absolute x = if x >= 0 then x
             else -x

-- int with smallest value
smallest :: Int -> Int -> Int
smallest a b = if a > b then b
               else a

-- incrementAllBy k xs means increment all elements by k
incrementAllBy :: Int -> [Int] -> [Int]
incrementAllBy _ [] = []
incrementAllBy k (x:xs) = (x * k) : incrementAllBy k xs

-- Change the tuple structure
changeTuple :: (Int, (Char, String)) -> ((Char, Int), String)
changeTuple (x,(y,z)) = ((y,x),z)

fizzBuzz :: [Int] -> [String]
fizzBuzz = undefined 

isAlphabetic :: Char -> Bool
isAlphabetic a = isAlpha a

-- hint: take, drop
substring :: Int -> Int -> String -> String 
substring = undefined 

combine :: [Int] -> [Char] -> [(Int, Char)]
combine = undefined

-- Functions

id :: Int -> Int
id x = x

sum :: Int -> Int -> Int
sum x y = x + y

mult :: (Int, Int) -> Int
mult (x, y) = x * y

toUpperAll :: [Char] -> [Char]
toUpperAll [] = []
toUpperAll (x:xs) = (toUpper x) : toUpperAll xs

reverseString :: [Char] -> [Char]
reverseString [] = ""
reverseString (x:xs) = (reverseString xs) ++ [x]

isPalindrome :: [Char] -> Bool
isPalindrome str = str == (reverseString str)

myMap :: (a -> b) -> [a] -> [b]
myMap f [] = []
myMap f (x:xs) = (f x) : (myMap f xs)

toUpperAll' = map toUpper

double :: Int -> Int
double x = let two = 2 
           in x * two

