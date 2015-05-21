from math import sqrt
""" Can actually do this much simpler way. just take the product of prime numbers while the product is less than the target (1,000,000)
    meaning 2*3*5*7*11*13*17 = 510510, same answer as this brute force solution
"""
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
        

highestToCheck = 1000001
maxPrimeGenerated = 0
generator = generatePrimes()
primes = []
p = next(generator)
while p < highestToCheck/2:
    primes.append(p)
    p = next(generator)

print("generated all primes")
def phi(n):
    #count = 0
    notRelativelyPrime = set()
    for prime in primes:
        if prime > n/2+1:
            break
        if n % prime == 0:
            temp = prime
            while temp < n:
                notRelativelyPrime.add(temp)
                temp += prime
    
    count = n-len(notRelativelyPrime)-1
    nphin = n / count
    #print( n, count, nphin )
    return nphin

maxTotient = 0.0
numberAtMaxTotient = 0
for i in range(2, highestToCheck):
    if i % 10000 == 0:
        print(i)
    p = phi(i)
    if p > maxTotient:
        maxTotient = p
        numberAtMaxTotient = i
        print( numberAtMaxTotient, maxTotient )
        
        
print("end!")
print( numberAtMaxTotient, maxTotient )

