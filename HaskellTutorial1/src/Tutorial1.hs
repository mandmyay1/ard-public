
import Data.Char

module Main where

main::IO()
main = putStrLn "Hello lol"

pyths n = [(x,y,z) | x <- [1..n], y <- [1..n], z <- [1..n], x^2+y^2 == z^2]


factors n = [x | x<- [1..n], n `mod` x == 0]

perfects n = [x | x<- [1..n], isPerfect x]
  where isPerfect num = sum (init (factors num)) == num

find k t = [v | (k',v) <- t, k == k']

positions x xs = find x (zip xs [0..n])
  where n = length xs -1
  
xls = 1 : [x + 1 | x <- xls]

riffle xs ys = concat [[x,y] | (x,y) <- xs `zip` ys]

divides x y = x `mod` y == 0
divisors x = [d | d <- [1..x], x `divides` d]



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



