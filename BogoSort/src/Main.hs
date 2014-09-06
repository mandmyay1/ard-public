
module Main where

import System.Random

shuffle :: String -> String
shuffle str = do
        let r = randomR (0, length str ) ( mkStdGen 4 )
        ret r
        "hello"
        
ret :: a -> IO a
ret a = putStrLn a

bogoSortRecurse :: String -> String -> Int -> Int
bogoSortRecurse str1 str2 count = if shuffle str1 == str2 then count else bogoSortRecurse str1 str2 count+1


bogoSort :: String -> String -> Int
bogoSort str1 str2 = bogoSortRecurse str1 str2 1

        

main::IO()
main = print (bogoSort "lolhe" "hello")

