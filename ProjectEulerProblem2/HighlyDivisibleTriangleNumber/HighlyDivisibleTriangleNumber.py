import functools
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



def primeFactors(num):
    listOfPrimeFactors = {}
    i = 1
    while num > 1:
        if is_prime(i) and num % i is 0 :
            if i in listOfPrimeFactors:
                listOfPrimeFactors[i] += 1
            else:
                listOfPrimeFactors[i] = 1
            #listOfPrimeFactors.append(i)
            num = num // i
            #i = max()
        else: i += 1
    return listOfPrimeFactors
        
        
currentTriangle = 0
i = 1
while True:
    currentTriangle = currentTriangle+i
    factors = primeFactors(currentTriangle)
    numFactors = 1
    for item in sorted(factors.values()):
        numFactors *= (1+item)
    if numFactors > 500:
        print( currentTriangle, i, numFactors )
        break
    i += 1
    
    