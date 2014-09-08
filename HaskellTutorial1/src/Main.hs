module Main where



main::IO()
main = do putStrLn "what is 2+2?"
          x <- readLn
          --sleepCycleEstimator x
          putStrLn x
                
                
--sleepCycleEstimator :: Int -> Int -> Bool -> Int -> Int -> Bool
--sleepCycleEstimator hr min ampm = 

convertTimeToString :: Int -> String
convertTimeToString t = show (t `div` 60) ++ ":" ++  show (t `mod` 60) ++ ""

convertTimeToStringWithAMPM :: Int -> String
convertTimeToStringWithAMPM t = if t > 720 then convertTimeToString (t-720) ++ " PM" else convertTimeToString t ++ " AM"


factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial( n-1 )

charname :: Char -> String
charname 'a' = "Adam"
charname 'b' = "Broseph"
charname 'c' = "Carlos"


addVectors :: (Num a) => (a,a) -> (a,a) -> (a,a)
addVectors (x1,y1) (x2,y2) = (x1+x2, y1+y2)
--addVectors a b = ( fst a + fst b, snd a + snd b )

first :: (a,b,c) -> a
first (a,_,_) = a 

second :: (a,b,c) -> b
second (_,b,_) = b

third :: (a,b,c) -> c
third (_,_,c) = c

head' :: [a] -> a
head' [] = error "Error need at least one element in list"
head' (x:xs) = x

tell :: (Show a) => [a] -> String
tell [] = "List is empty"
tell [x] = "List contains one element " ++ show x
tell [x,y] = "List contains 2 elements " ++ show x ++ " " ++ show y
tell (x:y:_) = "List is too long. First two elements are " ++ show x ++ " " ++ show y

length' :: [a] -> Int
length' [] = 0
length' (x:xs) = 1 + length' xs

sum' :: (Num a) => [a] -> a
sum' [] = 0
sum' (x:xs) = x + sum' xs

capital :: String -> String
capital [] = []
capital [a] = ['A' + a]









