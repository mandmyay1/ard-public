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


sizeOfSpiral = 7
startat = 1

movingUp = (0,1)
movingDown = (0,-1)
movingRight = (1,0)
movingLeft = (-1,0)

initialDirection = movingRight

x = 0
y = 0

diagonalPrimes = 0
diagonals = 0
ratioPrimes = 1.0
incrementor = 1
while ratioPrimes > .10:
    firstpass = True
    while startat <= sizeOfSpiral **2:
        initialLocation = (x,y)
        if x == y or x == -y:
            diagonals += 1
            if is_prime(startat):
                diagonalPrimes += 1
            
        startat += incrementor
        x += initialDirection[0]*incrementor
        y += initialDirection[1]*incrementor
        if initialDirection is movingRight:
            initialDirection = movingUp
            if not firstpass:
                initialLocation = (x,y)
                if x == y or x == -y:
                    diagonals += 1
                    if is_prime(startat):
                        diagonalPrimes += 1
                
                x += 1
                startat += 1
                incrementor +=1
                startat += incrementor 
                x += initialDirection[0]*incrementor
                y += initialDirection[1]*incrementor
                initialDirection = movingLeft
                incrementor += 1
            
        elif initialDirection is movingUp:
            initialDirection = movingLeft
            incrementor += 1
        elif initialDirection is movingLeft:
            initialDirection = movingDown
        elif initialDirection is movingDown:
            initialDirection = movingRight
            firstpass = False

    ratioPrimes = diagonalPrimes / diagonals
    
    print(ratioPrimes, sizeOfSpiral)
    sizeOfSpiral += 2

    
    