len [] = 0
len (x:xs) = 1 + len xs

double x = x + x

a = \x -> x+x
b = \x -> \y -> x+y
f g x = (g x) + 1

f :: Num b => (a -> b) -> a -> b
qs [] = []
qs (x:xs) = (qs [y | y<-xs, y<=x]) ++ [x] ++ (qs [y | y<-xs, y>x])

rs [] = []
rs (x:xs) = (rs [y | y<-xs, y>x]) ++ [x] ++ (rs [y | y<-xs, y<=x])

qqs s [] = []
qqs s (x:xs) = (qqs s [y | y<-xs, (s x y)] ++ [x] ++ (qqs s [y | y<-xs, not(s x y)]))

