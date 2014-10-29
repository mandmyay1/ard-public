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

def is_permutation(num1, num2):
    #print([''.join(i) for i in permutations(str(num2))])
    return str(num1) in [''.join(i) for i in permutations(str(num2))]

def has_equal_distances(listPermutations):
    for item in listPermutations:
        for item2 in listPermutations:
            if item2 is not item:
                dist = item2 - item
                if item2 + dist in listPermutations:
                    return [item, item2, item2+dist]
    return None

setPrimes = [i for i in range(1000,10000) if is_prime(i)]
#print(len(setPrimes));

#print( is_permutation(1487, 4817))
#print( is_permutation(1009, 1013))

listPermutations = {}
for prime in setPrimes:
    found = False
    for perm in listPermutations:
        if is_permutation(prime, perm):
            listPermutations[perm] = sorted(listPermutations[perm] + [prime])
            found = True
    if not found:
        listPermutations[prime] = [prime]
        
#print(listPermutations)
for perm in listPermutations:
    if len(listPermutations[perm]) > 2:
        equal_distances = has_equal_distances(listPermutations[perm])
        if equal_distances is not None:
            print(equal_distances)
#    if len(listPermutations[perm]) < 3 : del listPermutations[perm]
print(listPermutations)