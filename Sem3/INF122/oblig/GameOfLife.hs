-- Clear the screen
cls :: IO ()
cls = putStr "\ESC[2J"

{-
Position of each character on the
screen is given by a pair (x, y) of
positive integers, with (1, 1) being
the top-left corner.
-}

type Pos = (Int, Int)

{-
We can define a function that displays
a string at a given position by using
control characters to move the cursor
to this position.
-}

writeat :: Pos -> String -> IO ()
writeat p xs = do goto p
                  putStr xs

goto :: Pos -> IO ()
goto (x,y) = putStr ("\ESC[" ++ show y ++ ";" ++ show x ++ "H")


{-
For increased we allow the board size to be
modified.
-}

width :: Int
width = 20

height :: Int
height = 20

-- Represent the board as a list of (x, y) positions.

type Board = [Pos]

-- Example board
example :: Board
example = [(1, 1), (1, 2), (2, 2), (2, 3), (1, 3),
           (5, 1), (5, 2), (4, 2), (4, 1), (5, 3),
           (9, 10), (9, 11), (9, 12), (9, 13),
           (10, 10), (10, 11), (10, 12), (10, 13),
           (10, 20), (11, 20), (12, 20), (13, 20)]


{-
Display the living cells on the screen.
The library function sequence_ :: [IO a]  -> IO ()
performs actions in sequence, discarding their result
values and returning no result.
-}

showcells :: Board -> IO ()
showcells b = sequence_ [writeat p "0" | p <- b]

isAlive :: Board -> Pos -> Bool
isAlive b p = elem p b

isEmpty :: Board -> Pos -> Bool
isEmpty b p = not (isAlive b p)

-- Return the neighbours

neighbs :: Pos -> [Pos]
neighbs (x,y) = map wrap [(x-1, y-1), (x,   y-1),
                          (x+1, y-1), (x-1, y),
                          (x+1, y),   (x-1, y+1),
                          (x,   y+1), (x-1, y+1)]

{-
The auxiliary function wrap takes account of the wrapping
around at the edges of the board, by subtracting one from
each component of the given position, taking the reminder
when divided by the width and height of the board, and then
adding one to each component again.
-}

wrap :: Pos -> Pos
wrap (x,y) = (((x-1) `mod` width) + 1,
              ((y-1) `mod` height) + 1)


-- Calculate the number of live neighbours for a given position

liveneighbs :: Board -> Pos -> Int
liveneighbs b = length . filter (isAlive b) . neighbs

{-
Produce a list of living positions in a board that have
precisely 2 or 3 living neighbours, and hence survive to
the next generation of the game.
-}

survivors :: Board -> [Pos]
survivors b = [p | p <- b, elem (liveneighbs b p) [2,3]]

{-
List empty positions in a board that have precisely three living
neighbors, and hence give birth to a new cell.
-}

births :: Board -> [Pos]
births b = [p | p <- rmdups (concat (map neighbs b)),
                     isEmpty b p,
                     liveneighbs b p == 3]


-- Remove duplicates from a list

rmdups :: Eq a => [a] -> [a]
rmdups [] = []
rmdups (x:xs) = x : rmdups (filter (/= x) xs)


{-
New generation of the board is produced by appending
the list of survivors and the list of new births.
-}

nextgen :: Board -> Board
nextgen b = survivors b ++ births b


-- True/False is the Board Empty 

isBoardEmpty :: Board -> Bool
isBoardEmpty b = and [isEmpty b p | p <- rmdups (concat (map neighbs b))]


{-
 Game of life
 1. Clear screen
 2. Show living cells
 3. Wait for a moment
 4. Continue with the next generation
-}

life :: Board -> IO ()
life b = if not (isBoardEmpty b) then
            do cls
               showcells b
               wait 500000
               life (nextgen b)
         else
            do cls
               goto (1,1)
               putStrLn "Game Over !"


-- Slow down the game to a reasonable speed

wait :: Int -> IO ()
wait n = sequence_ [return () | _ <- [1..n]]