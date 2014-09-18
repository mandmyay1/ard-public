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

start = 2
listPrimes = []
while True:
    if is_prime(start):
        listPrimes.append(start)
    start += 1
    l = len(listPrimes)
    if l > 10001:
        break;
print(listPrimes[10000])