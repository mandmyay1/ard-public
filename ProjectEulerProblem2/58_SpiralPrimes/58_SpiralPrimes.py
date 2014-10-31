from math import sqrt

""" Do not use this one, it's more brute-force, and a lot slower than __init__.py"""

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


sizeOfSpiral = 7
startat = 1

movingUp = (0,1)
movingDown = (0,-1)
movingRight = (1,0)
movingLeft = (-1,0)

initialDirection = movingRight

setPrimes = set()
setNotPrime = set()

ourSpiral = {}
x = 0
y = 0

diagonalPrimes = 0
diagonals = 0
ratioPrimes = 1.0
while ratioPrimes > .10:
    while startat <= sizeOfSpiral **2:
        initialLocation = (x,y)
        ourSpiral[initialLocation] = startat
        if x == y or x == -y:
            diagonals += 1
            if is_prime(startat):
                diagonalPrimes += 1
            
        startat += 1
        x += initialDirection[0]
        y += initialDirection[1]
        if initialDirection is movingRight and not (x,y+1) in ourSpiral:
            initialDirection = movingUp
        elif initialDirection is movingUp and not (x-1,y) in ourSpiral:
            initialDirection = movingLeft
        elif initialDirection is movingLeft and not (x,y-1) in ourSpiral:
            initialDirection = movingDown
        elif initialDirection is movingDown and not (x+1,y) in ourSpiral:
            initialDirection = movingRight
        

    listEntriesToDelete = []
    for entry in ourSpiral.keys():
        if max(abs(entry[0]),abs(entry[1])) < x-2:
            listEntriesToDelete.append(entry)
    for entry in listEntriesToDelete:
        del ourSpiral[entry]
    
    ratioPrimes = diagonalPrimes / diagonals
    
    print(ratioPrimes, sizeOfSpiral)
    sizeOfSpiral += 2
"""
    for i in range(1,sizeOfSpiral//2+1):
        diagonals += 4
        d1 = ourSpiral[(i,i)]
        if d1 in setPrimes: diagonalPrimes += 1
        elif d1 in setNotPrime: pass
        elif is_prime(d1):
            setPrimes.add(d1)
            diagonalPrimes += 1
        else: setNotPrime.add(d1)
        
        d2 = ourSpiral[(-i,i)]
        if d2 in setPrimes: diagonalPrimes += 1
        elif d2 in setNotPrime: pass
        elif is_prime(d2):
            setPrimes.add(d2)
            diagonalPrimes += 1
        else: setNotPrime.add(d2)
        
        d3 = ourSpiral[(i,-i)]
        if d3 in setPrimes: diagonalPrimes += 1
        elif d3 in setNotPrime: pass
        elif is_prime(d3):
            setPrimes.add(d3)
            diagonalPrimes += 1
        else: setNotPrime.add(d3)
        
        d4 = ourSpiral[(-i,-i)]
        if d4 in setPrimes: diagonalPrimes += 1
        elif d4 in setNotPrime: pass
        elif is_prime(d4):
            setPrimes.add(d4)
            diagonalPrimes += 1
        else: setNotPrime.add(d4)"""
    
    