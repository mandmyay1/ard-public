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
        
def generateSquares():
    start = 1
    while True:
        yield start **2
        start += 1

squareGenerator = generateSquares()
setSquares = set()
maxSquare = next(squareGenerator)
while maxSquare < 1000:
    setSquares.add(maxSquare)
    maxSquare = next(squareGenerator)
    
primeGenerator = generatePrimes()
setPrimes = set()
maxPrime = next(primeGenerator)
while maxPrime < 1000:
    setPrimes.add(maxPrime)
    maxPrime = next(primeGenerator)



oddComposite = 9
while True:
    if maxPrime < oddComposite:
        setPrimes.add(maxPrime)
        maxPrime = next(primeGenerator)
    if maxSquare < oddComposite:
        setSquares.add(maxSquare)
        maxSquare = next(squareGenerator)
    found = False
    for prime in setPrimes:
        if found: break
        for square in setSquares:
            if oddComposite == prime + 2*square:
                found = True
                break
    if not found:
        print(oddComposite, "cannot be written as prime + 2*square")
        break
    oddComposite += 2
    while is_prime(oddComposite):
        oddComposite += 2
        
