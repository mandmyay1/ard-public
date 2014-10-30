from math import sqrt
from itertools import permutations

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


perms = set()
for perm in permutations('1234567', 7):
    perms.add("".join(perm))

perms = sorted(list(perms))
print(perms[0],perms[1])
for perm in reversed(perms):
    if is_prime(int(perm)):
        print( perm )
        break
    