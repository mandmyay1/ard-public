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


listPrimes = [i for i in range(1,1000000) if is_prime(i)]

maxPrime = max(listPrimes)

print(len(listPrimes))

currentHighestPrime = 0
currentNumber = 0
for i in range(len(listPrimes)):
    s = listPrimes[i]
    numCurrent = 1
    for j in range(i+1, len(listPrimes)):
        numCurrent += 1
        s += listPrimes[j]
        if s > maxPrime: break
        if s in listPrimes:
            if numCurrent > currentNumber:
                currentNumber = numCurrent
                currentHighestPrime = s
                print(currentHighestPrime, currentNumber)

print(currentHighestPrime, currentNumber)