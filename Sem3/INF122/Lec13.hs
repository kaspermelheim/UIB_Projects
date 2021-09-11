brett :: Int -> IO ()
brett nR = do clr 
              writeTop nR
              mapM_ (\i -> writeRow i nR) [1..nR]

clr :: IO ()
clr = putStr "\ESC[2J"

writeTop :: (Show a, Integral a) => a -> IO ()
writeTop nR =
    writeAt (lft + 1, 0) ((concat [(show (mod i 10)) ++ " " | i <- [1..nR]]) ++"\n")

lft :: Int
lft = 3

writeAt :: (Int, Int) -> String -> IO ()
writeAt (x,y) xs = do
    goto (x,y)
    putStr xs

goto :: (Int, Int) -> IO ()
goto (x,y) = putStr("\ESC["++show y++";"++show x++"H")

writeRow :: Int -> Int -> IO ()
writeRow i nR = do
    writeAt (if i > 9 then (lft - 2) else lft - 1, 1+i) (show i)
    mapM_ (\i -> putStr " .") [1..nR]
    putStrLn ""