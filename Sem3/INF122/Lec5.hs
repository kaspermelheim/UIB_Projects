{-Tar inn et tall n og liste, splitter lista på n og lager 2 lister-}
splitA :: Int -> [a] -> ([a],[a])
splitA n xs = (take n xs, drop n xs)

{-If else løkke som tar inn og sender ut boolean-}
og x y = if x == False then False
         else if y == False then False
            else True

{-Samme som over men annen måte å skrive if else på-}
ogg x y | x == False = False
        | y == False = False
        | otherwise = True

fil :: (a -> Bool) -> ([a] -> [a])
fil p [] = []
-- fil p (x:xs) = if (p x) == True then x: fil p xs else fil p xs
fil p (x:xs) | p x == True = x : fil p xs
             | otherwise = fil p xs

--Print alle partal opp til n
factors n = [ x | x <- [1..n], n `mod` x == 0 ]

--Sjek om n er et primtall
prime n = factors n == [1,n]

--Print alle primtal opp til n
primes n = [ x | x <- [1..n], prime x]

flatten ll = [e | l <- ll, e <- l]

--Tar inn en liste med mange delstringer, og setter det sammen til en string
fl [] = []
fl (x:xs) = x ++ (fl xs)

lup k ob = [ v | (c,v) <- ob, c==k ]

pairs l = zip l (tail l)

sorted l = and [x <= y | (x,y) <- pairs l]

posilist x xs = [ i | (v,i) <- (zip xs [1..length xs]), v == x ]




