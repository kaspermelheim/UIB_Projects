module INF122 where
goXup x = putStr $ "\ESC[" ++ show x ++ "A"
goXdown x = putStr $ "\ESC[" ++ show x ++ "B"
goYright y = putStr $ "\ESC[" ++ show y ++ "C"
goYleft y = putStr $ "\ESC[" ++ show y ++ "D"
deleteLineAtCursor = putStr "\ESC[2K"

lagBrett :: Int -> String
lagBrett size = let
    firRow = concat [show i ++ spaces2 i | i <- [1..size]]
    rad = concat $ replicate size "  ." in
        "    " ++ firRow ++ "\n" ++
        concat [show i ++ spaces i ++ rad ++ "\n" | i <- [1..size]]
    where
        spaces i | (i >= 10) = ""
                 | otherwise = " "
        spaces2 i | (i >= 9) = " "
                  | otherwise = "  "

brett size = putStr $ lagBrett size

-- B

main size = do
    brett size
    run size

run size = do
    line <- getLine
    goXup 1
    deleteLineAtCursor
    let lineWords = words line
    case lineWords of
        ("q":_) -> return ()
        ("n":x:y:_) -> do
            addX size (read x) (read y) 
            run size
        ("d":x:y:_) -> do
            delX size (read x) (read y)
            run size
        _ -> run size

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

addX :: Int -> Int -> Int -> IO ()
addX = doActionAt "\BSX"

delX :: Int -> Int -> Int -> IO()
delX = doActionAt "\BS."