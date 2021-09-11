--Lec 16

{-- 
{X = f(X) }
x = f(f(X)) = f (f(f(X))) = .... 
--}

{-- 
H : T

(:) H T
--}

(ø |- \x -> \y -> x*y :: t)

(           |- 0 :: t)     { t = Int }
(           |- 'c' :: t)   { t = Char }
(r, x :: tp |- x :: t)     { t = tp }

c -> e -> /= (c -> e) -> b