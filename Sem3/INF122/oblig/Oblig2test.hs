
module INF122 where
import Data.Char (isDigit)

type Cells = [(Int, Int)]
type BirthBounds = (Int, Int)
type SurviveBounds = (Int, Int)
type BoardSize = Int
type State = (Cells, BoardSize, SurviveBounds, BirthBounds)

--Gjør det mulig å legge til eller fjerne flere celler på en input eks. n 1 1 2 2 3 3 (legger til celle i (1,1), (2,2) og (3,3))
writeMult :: [(Int, Int)] -> Bool -> IO ()
writeMult [] b = return()
writeMult (x:xs) b = do
        if b then putStrLn (show x) else putStrLn (show x)
        writeMult xs b

newCell :: [[Bool]] -> [(Int, Int)] -> IO [Bool]
newCell grid xs = undefined


--Skriver til brettet på en bestemt koordinat
writeAt (x,y) xs = do
    goto (x,y)
    putStr xs

--Flytter oss til en spesifisert pos
goto :: (Int, Int) -> IO ()
goto (x,y) = putStr("\ESC["++show y++";"++show x++"H")


main2 :: State -> IO()
main2 state = do
    let (cells, size, survive, born) = state 
    brett size
    putStrLn $ "The current state is: " ++ show cells ++ show size ++ show survive ++ show born
    run2 cells
    return ()

run2 :: [(Int, Int)] -> IO()
run2 state = do
    line <- getLine
    goXup 1
    deleteLineAtCursor
    let lineWords = words line
    case lineWords of
        ("quit":_) -> return ()
        ("n":x:y:_) -> do
            --Print ny celle til brettet
            addX 10 (read x) (read y)
            let newState = (read x, read y):state 
            run2 newState
        ("e":x:y:_) -> do
            delX 10 (read x) (read y)
            let newState = (read x, read y):state 
            run2 newState

cells :: [(Integer, Integer)]
cells = [(1,1), (1,2),(1,3),(2,1),(2,2)]

testState :: State
testState = ([(2,3)], 5, (4,4), (4,1))

neigh (x,y) state = [(i,j) | i <- [x-1..x+1], j <- [y-1..y+1], (i,j) /= (x,y), (i,j) `elem` state]

--Standard rules:
--1. mindre enn 2 naboer = død
--2. 2 eller 3 naboer = lever til neste runde
--3. død celle med 3 naboer = reborn
--4. levende celle med 4 eller flere naboer = dør, overpopulasjon 

baseRules :: [(Integer, Integer)]
baseRules = [(2,3), (3,3)]

--Får inn en død celle for å sjekke om den kan bli født
canBeBorn :: [(Integer, Integer)] -> [(Integer, Integer)] -> Bool
canBeBorn xs (y:ys) = if len xs == fst y then True
               else False

--Sjeker om en levende celle kan leve, True dersom ja, False om nei (da dør den)
canLive :: [(Integer, Integer)] -> [(Integer, Integer)] -> Bool
canLive xs (y:ys) = if len xs == fst y || len xs == snd y then True
               else False

--Funksjon som sjekker lengden på en gitt liste
len :: Num p => [t] -> p
len [] = 0 
len xs = sum [1 | _ <- xs]

goXup :: Show a => a -> IO ()
goXup x = putStr $ "\ESC[" ++ show x ++ "A"

goXdown :: Show a => a -> IO ()
goXdown x = putStr $ "\ESC[" ++ show x ++ "B"

goYright :: Show a => a -> IO ()
goYright y = putStr $ "\ESC[" ++ show y ++ "C"

goYleft :: Show a => a -> IO ()
goYleft y = putStr $ "\ESC[" ++ show y ++ "D"

deleteLineAtCursor :: IO ()
deleteLineAtCursor = putStr "\ESC[2K"

--Lager et nytt tomt brett med størrelse size (Int)
c :: Int -> String
c size = let
    firRow = concat [show i ++ spaces2 i | i <- [1..size]]
    rad = concat $ replicate size "  ." in
        "    " ++ firRow ++ "\n" ++
        concat [show i ++ spaces i ++ rad ++ "\n" | i <- [1..size]]
    where
        spaces i | (i >= 10) = ""
                 | otherwise = " "
        spaces2 i | (i >= 9) = " "
                  | otherwise = "  "


l :: Int -> Int -> IO()
l x size = if x > 0 then do
           addX size x 2
           wait 500000
           l (x-1) size
           else run size baseRules

brett size = putStr $ c size

-- B
--Main funksjon som starter spillet
main :: Int -> IO ()
main size = do
    brett size
    run size baseRules

printRules :: IO ()
printRules = putStr $ show baseRules 

main3 = do
    line <- getLine
    let lw = words line
    case lw of
        ("quit":_) -> return ()
        ("c":x:_) -> do
            brett (read x)
            run (read x ) baseRules

run :: Int -> [(Integer, Integer)] -> IO ()
run size rules = do
    line <- getLine
    goXup 1
    deleteLineAtCursor
    let lineWords = words line
    case lineWords of
        ("quit":_) -> return ()
        ("n":x:y:_) -> do
            addX size (read x) (read y)
            run size baseRules
        ("e":x:y:_) -> do
            delX size (read x) (read y)
            run size rules
        ("l":x:_) -> do
            l (read x) size
        ("?":_) -> do
            putStr (show rules)
            run size rules
        --("r":file) -> do

        _ -> run size rules



--Enten legger til eller fjerner celle på brettet alt etter hva vi sender inn som act
doActionAt :: String -> Int -> Int -> Int -> IO()
doActionAt act size x y = do
    if x > size || y > size then
        return ()
    else do
        let mx = size - x + 1
            my = y * 3 + 2
        goXup mx
        goYright my
        putStr act  
        goXdown mx
       -- goYleft my

--Legger til en ny celle
addX :: Int -> Int -> Int -> IO ()
addX = doActionAt "\BSO"

--Fjerner en celle
delX :: Int -> Int -> Int -> IO()
delX = doActionAt "\BS."

--Får spillet til å gå et passelig tempo
wait :: Int -> IO ()
wait n = sequence_ [return () | _ <- [1..n]]
