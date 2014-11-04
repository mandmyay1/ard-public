import Data.Char

let2int :: Char -> Int
let2int c = ord c - ord 'a'

int2let :: Int -> Char
int2let n = chr (ord 'a' + n)

capLet2Int :: Char -> Int
capLet2Int c = ord c - ord 'A'

int2CapLet :: Int -> Char
int2CapLet n = chr (ord 'A' + n)

shift :: Int -> Char -> Char
shift n c
  | isLower c = int2let ((let2int c + n) `mod` 26)
  | isUpper c = int2CapLet ((capLet2Int c + n) `mod` 26)
  | otherwise = c
  
encode :: Int -> String -> String
encode n xs = [shift n x | x <- xs]


and' :: [Bool] -> Bool
and' [] = True
and' (b : bs)
  | b = b
  | otherwise = and' bs 
  
  
concat' [] = []
concat' (xs : xss) = xs ++ concat' xss

replicate' 0 _ = []
replicate' n x = x : replicate' (n-1) x


merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys)
  = if x <= y then x : merge xs (y:ys) else y : merge (x:xs) ys
  
halve xs = splitAt (length xs `div` 2) xs


msort [] = []
msort [x] = [x]
msort xs = merge (msort ys) (msort zs)
  where (ys, zs) = halve xs