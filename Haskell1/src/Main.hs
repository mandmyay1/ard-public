module Main where


main::IO()
main = putStrLn "Hello what is your name?" >> getLine >>= \name -> putStrLn( "hello " ++ name ++ "!" )

doubleMe x = x + x
doubleUs x y = doubleMe x + doubleMe y

doubleSmallNumber x = if x > 100 
                        then x 
                        else x*2
                        
boomBangs xs = [ if x < 10 then "Boom!" else "Bang!" | x <- xs, odd x ]

length' xs = sum[ 1 | _ <-xs ]

removeNonUpperCase :: [Char] -> [Char]
removeNonUpperCase st = [ c | c <- st, c `elem` ['A'..'Z'] ]

addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z

factorial :: Integer -> Integer
factorial x = product [1..x]

circumference :: Float -> Float
circumference r = 2 * pi * r

circumference' :: Double -> Double
circumference' r = 2 * pi * r

capital :: String -> String
capital "" = "Empty String"
capital all@(x:xs) = "The first character of " ++ all ++ " is " ++ [x]

bmiTell :: (RealFloat a) => a -> a -> String
bmiTell weight height
        | weight/height^2 <= 18.5 = "You're underweight"
        | weight/height^2 <= 25.0 = "You're supposedly normal"
        | weight/height^2 <= 30.0 = "You're overweight, fatass"
        | otherwise   = "You're a fat whale, congratsulatiopns"