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
setPrimes = []
while True:
    if is_prime(start):
        setPrimes.append(start)
    start += 1
    l = len(setPrimes)
    if l > 10001:
        break;
print(setPrimes[10000])