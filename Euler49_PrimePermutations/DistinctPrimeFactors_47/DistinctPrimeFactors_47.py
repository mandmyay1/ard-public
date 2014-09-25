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

def primeFactors(num):
    listOfPrimeFactors = {}
    global listPrimes
    i = 1
    while num > 1:
        if i in listPrimes and num % i is 0 :
            if i in listOfPrimeFactors:
                listOfPrimeFactors[i] += 1
            else:
                listOfPrimeFactors[i] = 1
            #listOfPrimeFactors.append(i)
            num = num // i
            #i = max()
        else: i += 1
    return listOfPrimeFactors

start = 1
while True:
    c1 = start
    c2 = start +1
    c3 = start +2
    c4 = start +3
    p1 = primeFactors(c1)
    if len(p1) is 4:
        p2 = primeFactors(c2)
        if len(p2) is 4:
            p3 = primeFactors(c3)
            if len(p3) is 4:
                p4 = primeFactors(c4)
                if len(p4) is 4:
                    print(c1, c2, c3, c4)
                    break
    start += 1