import System.IO

adder = do
    putStr "antallet: "
    ant <- getLine
    adde ((read ant) ::Int) 0

adde :: Int -> Int -> IO ()
adde ant sm = if ant == 0 then putStrLn ("Summen var "++ (show sm))
              else do tall <- getLine
                      adde (ant-1) (sm + ((read tall)::Int))
                    
add1 :: IO ()
add1 = addl 0

addl :: Int -> IO ()
addl sm = do
    antS <- getLine
    let ant = ((read antS)::Int)
    if ant == 0 then (print sm)
    else addl (sm+ant)