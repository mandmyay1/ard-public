from math import sqrt

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

def numberPrimesGenerated(a, b):
    """ n**2 + a*n + b """
    for n in range(0,100):
        val = n**2 + a*n + b
        if not is_prime(val):
            return n
    return -1

maxA = 0
maxB = 0
maxNumbers = 0
for a in range(-1000,1000):
    for b in range(-1000,1000):
        numberPrimesForEquation = numberPrimesGenerated(a, b)
        if( numberPrimesForEquation > maxNumbers ):
            maxNumbers = numberPrimesForEquation
            maxA = a
            maxB = b
            
print(maxNumbers, maxA, maxB, maxA*maxB)
