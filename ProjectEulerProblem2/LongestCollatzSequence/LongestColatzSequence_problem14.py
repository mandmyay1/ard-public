

maxStart = 1000000

def collatz(num):
    ret = 1
    if num is 1: return ret
    if num % 2 is 0:
        ret = 1+collatz(num//2)
    else:
        ret = 1+collatz(3*num+1)
    return ret

m = 0
startingNumber = 0
for i in range(1, maxStart):
    if i % 10000 is 0: print( "at " , i)
    curr = collatz(i)
    if curr > m:
        m = curr
        startingNumber = i
    
print(m, startingNumber)
#print(collatz(13))