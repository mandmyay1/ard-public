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
        

numbers = {'0','1','2','3','4','5','6','7','8','9'}
setPrimes = set()
generator = generatePrimes()
result = next(generator)
found8 = False
initialMax = 1
while not found8:
    initialMax *= 10
    setPrimes.clear()
    while result / initialMax < 1.0:
        setPrimes.add(result)
        result = next(generator)
    print(setPrimes)
    
    for prime in setPrimes:
        strPrime = str(prime)
        for number in numbers:
            #strPrime.
            pass
    
#print(setPrimes)