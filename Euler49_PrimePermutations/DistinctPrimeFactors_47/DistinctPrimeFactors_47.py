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

def generatePrimes():
    start = 2
    while True:
        if is_prime(start):
            yield start
        start += 1


generator = generatePrimes()
maxPrime = next(generator)
setPrimes = set()
while maxPrime < 1000000:
    setPrimes.add(maxPrime)
    maxPrime = next(generator)

def primeFactors(num):
    setOfPrimeFactors = set()
    global setPrimes
    global maxPrime
    i = 1
    while num > 1:
        if i > maxPrime and is_prime(i):
            setPrimes.add(i)
            maxPrime = i
        if i in setPrimes and num % i == 0 :
            setOfPrimeFactors.add(i)
            num = num // i
        else: i += 1
    return setOfPrimeFactors

start = 1
while True:
    c1 = start
    c2 = start +1
    c3 = start +2
    c4 = start +3
    p4 = primeFactors(c4)
    if len(p4) is 4:
        p3 = primeFactors(c3)
        if len(p3) is 4:
            p2 = primeFactors(c2)
            if len(p2) is 4:
                p1 = primeFactors(c1)
                if len(p1) is 4:
                    print(c1, c2, c3, c4)
                    break
            else: start = c2
        else: start = c3
    else: start = c4
    start += 1