import Data.List
import Data.Char
import Unsafe.Coerce

data Nat = Zero
         | Succ Nat
         deriving Show
         
nat2Integer (Succ n) = nat2Integer n + 1
nat2Integer Zero = 0

integer2Nat 0 = Zero
integer2Nat (n+1) = Succ (integer2Nat n)

add Zero n = n
add (Succ m) n = Succ (add n m)

mult m Zero = Zero
mult m (Succ n) = add m (mult m n)

data Tree = Leaf Integer
          | Node Tree Integer Tree

tree1 = Node (Node (Leaf 1) 3 (Leaf 4))
        5
        (Node (Leaf 6) 7 (Leaf 9))
        
occurs m (Leaf n) = m == n
occurs m (Node l n r)
  = case compare m n of
        LT -> occurs m l
        EQ -> True
        GT -> occurs m r

occurs4 :: Integer -> Tree -> Bool
occurs4 m (Leaf n) = m == n
occurs4 m (Node l n r)
  | m == n = True
  | m < n = occurs m l
  | otherwise = occurs m r
  
occurs5 m n = m == n
occurs5 m (Node l n r)
  | m == n = True
  | m > n = occurs m l
  | otherwise = occurs m r
  
data BTree = Leaf Integer
           | Node BTree BTree

tree2 = Node (Node (Leaf 1) (Leaf 3) ) (Node (Leaf 5) (Leaf 7))
tree3 = Node (Node (Leaf 1) (Leaf 2) ) (Leaf 3)
balanced :: BTree -> Bool

  