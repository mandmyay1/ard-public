data BTree = Leaf Integer
           | Node BTree BTree
           deriving Show

tree2 = Node (Node (Leaf 1) (Leaf 3) ) (Node (Leaf 5) (Leaf 7))
tree3 = Node (Node (Leaf 1) (Leaf 2) ) (Leaf 3)

leaves (Leaf _) = 1
leaves (Node l r) = leaves l + leaves r
balanced :: BTree -> Bool
balanced (Leaf _) = True
balanced (Node l r) 
  = abs (leaves l - leaves r) <= 1 && balanced l && balanced r
  
balance :: [Integer] -> BTree
halve xs = splitAt (length xs `div` 2) xs
balance [x] = Leaf x
balance xs = Node (balance ys) (balance zs)
  where (ys, zs) = halve xs
  
removeone :: Eq a => a -> [a] -> [a]
removeone x [] = []
removeone x (y:ys)
  | x == y = ys
  | otherwise = y : removeone x ys
  
isChoice :: Eq a => [a] -> [a] -> Bool
--isChoice [] _ = True
--isChoice (x:xs) [] = False
--isChoice (x:xs) ys = elem x ys && isChoice (removeone x xs) ys
isChoice [] _ = True
isChoice (x:xs) [] = False
isChoice (x:xs) ys = elem x ys && isChoice xs (removeone x ys)