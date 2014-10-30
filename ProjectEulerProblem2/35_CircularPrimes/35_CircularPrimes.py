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
        
def allRotationsInList(num, listPrimes):
    strNum = str(num)
    strComb = strNum[1:] + strNum[0]
    while strComb != strNum:
        if int(strComb) not in listPrimes:
            return False
        strComb = strComb[1:] + strComb[0]
    return True
    
print( allRotationsInList(37, [37,4,73]))

primeGenerator = generatePrimes()
maxPrime = next(primeGenerator)
setPrimes = set()
while maxPrime < 1000000:
    setPrimes.add(maxPrime)
    maxPrime = next(primeGenerator)
    
listPrimes = sorted(list(setPrimes))
print(len(listPrimes), listPrimes[0], listPrimes[len(listPrimes)-1])

total = 0
for prime in listPrimes:
    if allRotationsInList(prime, setPrimes):
        print(prime,"is all rotations")
        total +=1
        
print(total)

