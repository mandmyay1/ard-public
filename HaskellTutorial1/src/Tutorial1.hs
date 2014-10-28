module Main where

main::IO()
main = putStrLn "Hello lol"

n::Int
n = a `div` length xs
  where
        a = 10
        xs = [1,2,3,4,5]

last' xs = reverse xs !! (length xs -1 )

init' xs = drop (length xs -1 ) xs

qsort' [] = []
qsort' (x:xs)
  = reverse
      (reverse (qsort' smaller) ++ [x] ++ reverse (qsort' larger))
  where smaller = [a|a<-xs, a<=x]
        larger = [b|b<-xs, b>x]
        
        
second' xs = head (tail xs)
swap' (x,y) = (y,x)
pair' x y = (x,y)
double' x = x * 2
palindrome xs = reverse xs == xs
twice f x = f (f x)

f xs = take 3 (reverse xs)

halve xs = (take n xs, drop n xs)
  where n = length xs `div` 2

safetail
  = \ xs ->
      case xs of
           [] -> []
           (_ : xs) -> xs

mult = \ x -> (\ y -> (\ z-> x*y*z))
remove n xs = take n xs ++ drop (n+1) xs

funct :: Int -> [a] ->[a]
funct x xs = take (x+1) xs ++ drop x xs
e6 x y = x * y
e9 [x, y] = (x, True)
e10 (x, y) = [x, y]
e13 x = x * x

--e15 :: [a] -> [b] -> (a, b)
e15 xs ys = (head xs, head ys)



