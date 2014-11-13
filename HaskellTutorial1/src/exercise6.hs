--import Data.Bits


all' p xs = and (map p xs)
all2 p = and . map p
all3 p = not . any (not . p)
--all4 p = map p . and
all5 p xs = foldl (&&) True (map p xs)
all6 p xs = foldr (&&) False (map p xs)
all7 p = foldr (&&) True . map p

--any1 p = map p . or
any2 p = or . map p
any3 p xs = length (filter p xs) > 0
any4 p = not . null . dropWhile (not . p)
any5 p = null . filter p
any6 p xs = not (all (\ x -> not (p x)) xs)
any7 p xs = foldr (\ x acc -> (p x) || acc) False xs
any8 p xs = foldr (||) True (map p xs)

takeWhile1 _ [] = []
takeWhile1 p (x:xs)
  | p x = x : takeWhile1 p xs
  | otherwise = []
  
map1 f = foldr (\ x xs -> xs ++ [f x]) []
map2 f = foldr (\ x xs -> f x ++ xs) []
map3 f = foldl (\ xs x -> f x : xs) []
map4 f = foldl (\ xs x -> xs ++ [f x]) []

filter1 p = foldl (\ xs x -> if p x then x:xs else xs) []
filter2 p = foldr (\ x xs -> if p x then x:xs else xs) []
filter3 p = foldr (\ x xs -> if p x then xs ++ [x] else xs) []
--filter4 p = foldl (\ x xs -> if p x then xs ++ [x] else xs) []

dec2int1 = foldr (\ x y-> 10*x + y) 0
dec2int2 = foldl (\ x y-> x + 10*y) 0
dec2int3 = foldl (\ x y-> 10*x + y) 0
dec2int4 = foldr (\ x y-> x + 10*y) 0

--sumsqreven = compose [sum, map (^2), filter even]

--compose :: [a->a] -> (a -> a)
--compose = foldr (.) id

curry1 f = \ x y -> f x y
curry2 f = \ x y -> f
curry3 f = \ x y -> f (x, y)
curry4 f = \ (x,y) -> f x y

unfold p h t x
  | p x = []
  | otherwise = h x : unfold p h t (t x)
  
int2bin1 = unfold (== 0) (`mod` 2) (`div` 2)

--chop8 :: [Bit] -> [[Bit]]
chop8 [] = []
chop8 bits = take 8 bits : chop8 (drop 8 bits)

--chop81 = unfold [] (drop 8) (take 8)
chop82 = unfold null (take 8) (drop 8)
chop83 = unfold null (drop 8) (take 8)
chop84 = unfold (const False) (take 8) (drop 8)

unfmap1 f = unfold null (f) tail
unfmap2 f = unfold null (f (head)) tail
unfmap3 f = unfold null (f . head) tail
--unfmap4 f = unfold empty (f . head) tail

iterate1 f = unfold (const False) id f
iterate2 f = unfold (const False) f f
iterate3 f = unfold (const True) id f
iterate4 f = unfold (const True) f f















