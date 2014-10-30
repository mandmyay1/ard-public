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
        
def isTruncatableAndStillPrime(num, setPrimes):
    strNum = str(num)
    while len(strNum) > 0:
        if int(strNum) not in setPrimes:
            return False
        strNum = strNum[1:]
        
    strNum = str(num)
    while len(strNum) > 0:
        if int(strNum) not in setPrimes:
            return False
        strNum = strNum[:-1]
    return True

primeGenerator = generatePrimes()
setPrimes = set()
maxPrime = next(primeGenerator)
setPrimes = set()
while maxPrime < 1000000:
    setPrimes.add(maxPrime)
    maxPrime = next(primeGenerator)

listPrimes = sorted(list(setPrimes))
print(isTruncatableAndStillPrime(37, setPrimes))
listTruncatables = []
for prime in listPrimes:
    if prime < 10: continue
    if isTruncatableAndStillPrime(prime, setPrimes):
        listTruncatables.append(prime)

print(sum(listTruncatables), len(listTruncatables), listTruncatables)
#while len(listTruncatables) < 11:
    