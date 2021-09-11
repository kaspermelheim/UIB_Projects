-- Kasper Melheim

-- 2.4 løsning: fikk ikke brettet til å kjøre men kom fram til at mønsteret må være på formen: 10 (s 0 0, b 2 2) 2 2 3 3 4 3 5 2

--Oblig 2

------ | README | ------
{--

Start spillet med "main" i terminalen. Du kan nå skrive inn de ulike kommandoene og teste funksjonalitet. "Enter" er ikke implement, alt annet fungerer.

Har ikke fått spilet til å fungere 100%, men jeg har implementert alle brukerinput kommandoer som skal skje, og all funksjonalitet fungerer sånn som det skal
untatt selve spillet og algoritmen som skal sjekke dette. Føle likevel jeg skal få utteling for dette siden jeg har implementert funksjoner som tar inn en celle
og en liste av dens naboer, og sjekker om den får lov til å leve, dø eller skal bli gjenfødt på en god måte via disse. Har og implementert en neighbours funksjon,
denne sjekker naboene rundt en celle (x-1,x+1) og (y-1,y+1) f.feks, og denne fungerer som den skal så mye av funksjonaliteten er der, har bare ikke fått satt det 
i gang som et spill enda.

Lesing fra fil fungerer 100% og printer rett brett, main og run funksjon binder alle funksjonene sammen og sette i gang det som skal til ønskelig tid.
Brettet blir printet på en god måte, og fungerer for size>10 (så lenge brettet er mindre enn terminalen). Har og funksjoner som tar seg av multiple inputs
feks om du vil plassere 3 celler på en gang, samme om du vil fjerne. Har laget String -> Tup funksjon som gjør om fra string til tuple (veldig nyttig).

Implementert mange ulike hjelpefunksjoner nedover som fungerer som de skal.

Har brukt en del >>= og virkelig sett nyttgiheten av denne. 

Alt av plasseringer av O og . , oppbygging av brettet, plassering av input og putStr som blir printet ut er skalert med goto() og plassert på en ryddig og oversiktlig måte.
Ingenting blir feilplassert. 

Det er og mulig å endre på reglene med s x y og b x y, skriv så inn ? for å på oppdaterte regler i terminalen.

Brukte og litt kode fra forelesninger og tidligere ukesoppg.
-}

----- | Brett | -----

--Setter sammen brettet med en gitt str
gameBoard :: Int -> IO [[Bool]]
gameBoard 0 = error "Size of board cannot be 0"
gameBoard a = do 
              clr 
              goto (0,0)
              writeTop a
              mapM_ (\i -> writeRow i a) [1..a]
              return (take a $ repeat $ take a $ repeat False)

--Printer den øverste raden til terminalen
writeTop :: (Show a, Integral a) => a -> IO ()
writeTop a =
    writeAt (lft + 1, 0) ((concat [(show (mod i 10)) ++ " " | i <- [1..a]]) ++"\n")

lft :: Int
lft = 3

--WriteAt funk som bygger opp brettet
writeAt :: (Int, Int) -> String -> IO ()
writeAt (x,y) [] = error "Empty string cannot be written on board"
writeAt (x,y) xs = do
    goto (x,y)
    putStr xs



----- | Div og Hjelpefunksjoner | -----

--Clear
clr :: IO ()
clr = putStr "\ESC[2J"

--Fjerne alt på en linje
clear :: IO ()
clear = putStr "\ESC[2K"

--Gjør om fra String til Tuple
strToTup :: [String] -> [(Int, Int)]
strToTup [] = []
strToTup [_] = []
strToTup (x:y:xs) = ((read x), (read y)):(strToTup xs)

--Funksjon som sjekker lengden på en gitt liste
len :: Num p => [t] -> p
len [] = 0 
len xs = sum [1 | _ <- xs]

--Får spillet til å gå et passelig tempo
wait :: Int -> IO ()
wait n = sequence_ [return () | _ <- [1..n]]



----- | Funksjonalitet | -----

--Gjør det mulig å legge til eller fjerne flere celler på en input eks. n 1 1 2 2 3 3 (legger til celle i (1,1), (2,2) og (3,3))
multInput :: [(Int, Int)] -> Bool -> IO ()
multInput [] b = return()
multInput (x:xs) b = do
        if b then placeAt x "0" else placeAt x "."
        multInput xs b

--PlaceAt funk som tar seg av rett plassering av celler på brettet, når de dør og blir fødd
placeAt :: (Int, Int) -> String -> IO ()
placeAt (x,y) [] = error "Empty string cannot be written on board"
placeAt (x,y) xs = do
    goto (x*2+2,y+1)
    putStr xs

--Flytter oss til en gitt posisjon
goto :: (Int, Int) -> IO ()
goto (x,y) = putStr("\ESC["++show y++";"++show x++"H")

--Printer rader til terminalen
writeRow :: Int -> Int -> IO ()
writeRow i nR = do
    writeAt (if i > 9 then (lft - 2) else lft - 1, 1+i) (show i)
    mapM_ (\i -> putStr " .") [1..nR]
    putStrLn ""

--Funksjon som lager en ny celle og returnerer sånn det nye brettet vil se ut
addCell :: [[Bool]] -> [(Int,Int)] -> IO [[Bool]]
addCell grid xs = do
    multInput xs True
    let boardCopy = map (\(row, y) -> map (\(board, x) -> if (x,y) `elem` xs then True else board) (zip row [0..])) (zip grid [0..])
    return boardCopy

--Funksjon som fjerner en levende celle og returnerer sånn det nye brettet vil se ut
delCell :: [[Bool]] -> [(Int,Int)] -> IO [[Bool]]
delCell grid xs = do
    multInput xs False
    let boardCopy = map (\(row, y) -> map (\(board, x) -> if (x,y) `elem` xs then False else board) (zip row [0..])) (zip grid [0..])
    return boardCopy

neighbours :: (Num a, Num b, Enum a, Enum b, Eq a, Eq b, Foldable t) => (a, b) -> t (a, b) -> [(a, b)]
neighbours (x,y) state = [(i,j) | i <- [x-1..x+1], j <- [y-1..y+1], (i,j) /= (x,y), (i,j) `elem` state]

--Får inn en død celle for å sjekke om den kan bli født
--(y:ys) er reglene som gjelder
canBeBorn :: [(Integer, Integer)] -> [(Integer, Integer)] -> Bool
canBeBorn xs (y:ys) = if len xs == fst y then True
               else False

--Sjeker om en levende celle kan leve, True dersom ja, False om nei (da dør den)
--(y:ys) er reglene som gjelder
canLive :: [(Integer, Integer)] -> [(Integer, Integer)] -> Bool
canLive xs (y:ys) = if len xs == fst y || len xs == snd y then True
               else False

--Live funksjon som automatisk setter spillet i gang
live :: Int -> Int -> (Integer, Integer) -> (Integer, Integer) -> [[Bool]] -> IO()
live x size s b board = if x > 0 then do
           multInput [(x+1,x-1)] True
           wait 500000
           live (x-1) size s b board
           else run size s b board

readFromFile :: String -> IO [String]
readFromFile name = do  
        file <- readFile name
        return (words [x | x <- file, not (elem x ",()")])



----- | Main og Run | -----

--Main funksjon som setter spillet i gang
main :: IO()
main = do
    line <- getLine
    let l = words line
    case l of
        ("quit":_) -> return ()
        --Lag brettet med ønsket størrelse x
        ("c":x:_) -> do
            gameBoard (read x) >>= \bo2 -> run (read x) (2,3) (3,3) bo2
        ("r":xs) -> readFromFile (head xs) >>= \(size:s:x:y:b:i:j:xs) -> gameBoard (read size) >>= \board1 -> addCell board1 (strToTup xs) >>= \board2 -> run (read size) (read x,read y) (read i,read j) board2

--Run som blir kalt på fra main funksjonen, her blir de fleste inputa sjekket, og rett funksjoner blir kalt på for å gjør ønskelige endringer
run :: Int -> (Integer, Integer) -> (Integer, Integer) -> [[Bool]] -> IO ()
run size s b board = do
        goto(0, size + 2)
        clear
        putStr ""
        input <- getLine
        let index = words input
        case index of
            ("quit":_) -> return ()
            ("n":xs) ->
                addCell board (strToTup xs) >>= \br -> run size s b br
                --multInput (tup xs) True >> run size s b
            ("e":xs) ->
                delCell board (strToTup xs) >>= \br -> run size s b br
                --multInput (strToTup xs) False >> run size s b board
            ("b":x:y:_) ->
                run size (read x, read y) b board
            ("s":x:y:_) ->
                run size s (read x, read y) board
            ("l":x:_) -> do
                live (read x) size s b board
            --Printer rules til terminalen, må bruke denne for å oppdatere rules i terminalen dersom de endres
            ("?":_) -> do
                print (s,b)
                >> run size s b board
            ("r":xs) -> readFromFile (head xs) >>= \(size:s:x:y:b:i:j:xs) -> gameBoard (read size) >>= \board1 -> addCell board1 (strToTup xs) >>= \board2 -> run (read size) (read x,read y) (read i,read j) board2
            ("w":_) -> do
                print (s,b)
                >> run size s b board
            _ -> run size s b board

            

----- | Testdata | -----

testCells :: [(Integer, Integer)]
testCells = [(1,1), (1,2),(1,3),(2,1),(2,2)]

--Standard rules of Game of Life
baseRules :: [(Integer, Integer)]
baseRules = [(2,3), (3,3)]