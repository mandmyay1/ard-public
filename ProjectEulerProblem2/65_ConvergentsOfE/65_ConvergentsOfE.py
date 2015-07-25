from fractions import Fraction

def getNextSequence():
    k = 1
    ret = [1,2*k,1]
    
    while True:
        if len(ret) is 0:
            k+=1
            ret = [1, 2*k, 1]
        yield ret.pop(0)
        
a0 = 2
t1 = a0

generator = getNextSequence()
continued = [next(generator) for i in range(99)]
continued.reverse()

f = 0
for n in continued:
    denom = n + f
    f = Fraction(1, denom)

val = sum([int(c) for c in str((a0+f).numerator)])
print(val)
