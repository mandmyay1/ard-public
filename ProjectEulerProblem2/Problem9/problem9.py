from math import sqrt

"""find the sum of all primes below 2million"""

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


m = 10
start = 2
s = 0
while start < m:
    if is_prime(start): s += start
    start += 1
    
print(s)