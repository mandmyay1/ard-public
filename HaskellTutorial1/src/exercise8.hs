
putStr' :: String -> IO ()
putStr' [] = return ()
putStr' (x:xs) = putChar x >> putStr' xs

putStrLn1 [] = putChar '\n'
putStrLn1 xs = putStr' xs >> putStrLn1 ""

putStrLn2 [] = putChar '\n'
putStrLn2 xs = putStr' xs >> putChar '\n'

putStrLn3 [] = putChar '\n'
putStrLn3 xs = putStr' xs >>= \ x -> putChar '\n'

putStrLn4 [] = putChar '\n'
putStrLn4 xs = putStr' xs >> putStr' "\n"

putStrLn5 [] = putChar '\n'
putStrLn5 xs = putStr' xs >> putStrLn5 "\n"



getline' = get ""

get :: String -> IO String
get xs
  = do x <- getChar
       case x of
            '\n' -> return (x:xs)
            _ -> get (xs ++ [x])
            
---
sequence_' :: Monad m => [m a] -> m ()
sequence_' ms = foldr (>>) (return ()) ms

sequence' :: Monad m => [m a] -> m [a]
sequence' [] = return []
sequence' (m:ms)
  = m >>=
      \ a ->
        do as <- sequence' ms
           return (a:as)

sequence'1 :: Monad m => [m a] -> m [a]
sequence'1 ms = foldr func (return []) ms
  where
        func :: (Monad m) => m a -> m [a] -> m [a]
        func m acc
          = do x <- m
               xs <- acc
               return (x:xs)

sequence'2 :: Monad m => [m a] -> m [a]
sequence'2 [] = return []
sequence'2 (m:ms)
  = do a <- m
       az <- sequence'2 ms
       return (a:az)

(+++) a = do putChar a
             if a == 'a' then return True
             else return False
             
mapM' f [] = return []
mapM' f (a:as) 
  = f a >>= 
      \ b -> 
        do bs <- mapM' f as
           return (bs ++ [b])

filterM' :: Monad m => (a -> m Bool) -> [a] -> m [a]
filterM' _ [] = return []
filterM' p (x:xs)
  = do flag <- p x
       ys <- filterM' p xs
       if flag then return (x:ys) else return ys

(++++) a = do putChar a
              return a
liftM1 f m = m >> \ a -> return (f a)














