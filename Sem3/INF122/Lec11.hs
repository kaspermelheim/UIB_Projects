import Data.Char
import Data.List

lexx a b = if a<b then LT else if a>b then GT else EQ

lgh a b = if length a < length b then LT
          else if length a > length b then GT else EQ

sr pred ls = sortBy pred ls

(.) :: (b -> c) -> (a -> b) -> (a -> c)

ci :: (a -> b -> c) -> a -> (b -> c)
ci f g = \x -> f g x

tw = \f -> \x -> f (f x)

f = \x -> x + 1

g = f . f . f
