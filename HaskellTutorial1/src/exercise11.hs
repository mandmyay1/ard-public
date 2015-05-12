
fibs :: [Integer]
fibs = 0:1: [x+y | (x,y) <- zip fibs (tail fibs)]

fib n = fibs !! n

largeFib = head (dropWhile (<=1000) fibs)

data Tree a = Leaf
            | Node (Tree a) a (Tree a)
            
repeat :: a -> [a]
repeat x = xs
  where xs = x:xs