{-# OPTIONS_GHC -Wincomplete-patterns #-}

module Uke05Gruppe7 where

--------------------------------------------------------------------------------
-- Oppgave 1 -------------------------------------------------------------------

data Ast
  = V Int
  | P Ast Ast
  | M Ast Ast
  | W String -- (oppgave 3)
  deriving Show

eval :: Ast -> Int
eval (V n) = n
eval (P x y) = eval x + eval y
eval (M x y) = eval x * eval y
eval (W w) = error ("cannot evaluate `" ++ w ++ "`") -- (oppgave 3)


--------------------------------------------------------------------------------
-- Oppgave 2 -------------------------------------------------------------------

{-
Formen på syntaks-treet bestemmer hvor parentesene skal være. Det aritmetiske
uttrykket a + b + c kan representeres som et Ast på to måter:
  +           +
 / \         / \
a   +       +   c
   / \     / \
  b   c   a   b
med parentesuttrykk henholdsvis a + (b + c) og (a + b) + c
-}

innP :: Ast -> String
innP (V n) = show n
innP (P x y) = "(" ++ innP x ++ " + " ++ innP y ++ ")"
innP (M x y) = "(" ++ innP x ++ " * " ++ innP y ++ ")"
innP (W w) = w -- (oppgave 3)

{- Vi kan gjøre det litt penere ved å utelate parenteser på den ytterste noden
i treet ved hjelp av følgende definisjon, men det er ikke nødvendig. -}
inn :: Ast -> String
inn (P x y) = innP x ++ " + " ++ innP y
inn (M x y) = innP x ++ " * " ++ innP y
inn ast = innP ast

{- testing av inn: -}
innTest f =
  [ {- 5 -}
    f (V 5)
  , {- 55 + (2 * 3) -}
    f (P (V 55) (M (V 2) (V 3)))
  , {- (12 + 3) * (2 * 5) -}
    f (M (P (V 12) (V 3)) (M (V 2) (V 5)))
  , {- (((2 * 3) + 4) + (5 * 6)) * (7 + 8) -}
    f (M (P (P (M (V 2) (V 3)) (V 4)) (M (V 5) (V 6))) (P (V 7) (V 8)))
  , {- ((1 + 2) + 3) + 4 -}
    f (P (P (P (V 1) (V 2)) (V 3)) (V 4))
  , {- 1 + (2 + (3 + 4)) -}
    f (P (V 1) (P (V 2) (P (V 3) (V 4))))
  ]


--------------------------------------------------------------------------------
-- Oppgave 3 -------------------------------------------------------------------

{- Gramatikken har:
  Terminale symboler: {*, +, siffer, bokstav, (mellomrom)}
  Ikke-terminale symboler: {U, Tall, S, Ord, B}
  Start-symbol U
Gramatikken gitt i oppgaven beskriver ikke tokens, det er noe vi må finne ut av
selv. Personlig så foretrekker jeg å se på det som to gramatikker, en for
uttrykk og en for tokens:
  Gramatikk for uttrykk:
    U -> * U U | + U U | Tall | Ord
  Gramatikk for tokens:
    Token -> Tall | Ord | + | * | (mellomrom)
    Tall -> S Tall | S
    S -> siffer
    Ord -> B Ord | B
    B -> bokstav
da er gramatikken for uttrykk forenklet:
  Terminale symboler: {*, +, Tall, Ord}
  Ikke-terminale symboler: {U}
  Start-symbol U -}

-- Oppgave 3.1

tokenize :: [Char] -> [String]
tokenize [] = []
tokenize (' ' : s) = tokenize s
tokenize ('+' : s) = "+" : tokenize s
tokenize ('*' : s) = "*" : tokenize s
tokenize (c : s)
  | isDigit c =
    let (cs, s') = collectWhile isDigit s
     in (c : cs) : tokenize s'
  | isAlpha c =
    let (cs, s') = collectWhile isAlpha s
     in (c : cs) : tokenize s'
  | otherwise = error ("unexpected character " ++ show c)

collectWhile :: (Char -> Bool) -> String -> (String, String)
collectWhile p s = (takeWhile p s, dropWhile p s)
{- Den generaliserte versjonen av collectWhile er
  span :: (a -> Bool) -> [a] -> ([a], [a])
som er en predefinert funksjon. -}

isDigit, isAlpha :: Char -> Bool
isDigit c = c `elem` ['0' .. '9']
isAlpha c = c `elem` ['a' .. 'z'] ++ ['A' .. 'Z']
{- Du finner også disse funksjonene i Data.Char. Jeg er muligens for streng
siden funksjonen ikke tillater {æ,ø,å} -}

-- Oppgave 3.2

{- Parsingfunksjonen vår parser en liten bit av input og returnerer det sammen
med resten av input. Alle likningene har mønster på formen _ : _, dvs. at vi kun
trenger å se ett tegn fremover for å bestemme hvordan vi parser (LL(1)) -}
parseU :: [String] -> (Ast, [String])
parseU ("+" : s0) =
  let (e1, s1) = parseU s0
      (e2, s2) = parseU s1
   in (P e1 e2, s2)
parseU ("*" : s0) =
  let (e1, s1) = parseU s0
      (e2, s2) = parseU s1
   in (M e1 e2, s2)
parseU (t : ts)
  | isNumToken t = (V (read t), ts)
  | isWordToken t = (W t, ts)
  | otherwise = error ("unrecognized token " ++ show t)
parseU [] = error "unexpected end of input"

isNumToken, isWordToken :: String -> Bool
isNumToken xs = takeWhile isDigit xs == xs
isWordToken xs = takeWhile isAlpha xs == xs
{- se også funksjonen
  all :: (a -> Bool) -> [a] -> Bool
-}

{- Det er viktig at parseren ikke aksepterer en streng med ekstra input. F.eks.
bør ikke parse "+ 1 2 boom" være lovlig, siden
  parseU "+ 1 2 boom" = ( P (V 1) (V 2), ["boom"] )
-}
parse :: String -> Ast
parse s =
  case parseU (tokenize s) of
    (e, []) -> e
    (_, t : _) -> error ("unexpected token " ++ show t)

-- Oppgave 3.3

{- Vi har funksjoner
  parse :: String -> Ast
og
  eval :: Ast -> Int
som vi kan koble sammen med komposisjon for å lage ev. NB! Husk å oppdatere
ligningene for eval etter å ha lagt til konstruktøren W i definisjonen av Ast.
-}
ev :: String -> Int
ev s = eval (parse s)

evTest =
  [ (ev "+ * 2 3 4", 10)
  , (ev "+ * 2 3 + 1 4", 11)
  , (ev "+++1 2 3 4", 10)
  , (ev "* + 5 + 6 3 7", 98)
  ]

-- Oppgave 3.4

{- Tilsvarende som for ev -}
innfiks :: String -> String
innfiks s = inn (parse s)

innfiksTest =
  [ (innfiks "* 2 + 3 44", "2 * (3 + 44)")
  , (innfiks "* + 2 33 4", "(2 + 33) * 4")
  , (innfiks "+++1 2 3 4", "((1 + 2) + 3) + 4")
  , (innfiks "* + 5 + 6 3 7", "(5 + (6 + 3)) * 7")
  ]