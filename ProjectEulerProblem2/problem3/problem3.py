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



inp = 2520#600851475143

listOfPrimeFactors = []

i = 1
while inp > 1:
#for i in range(1,inp):
    #if i % 100000 is 0: print( "at ", i, listOfPrimeFactors)
    if is_prime(i) and inp % i is 0 :
        listOfPrimeFactors.append(i)
        inp = inp // i
        #i = max()
    else: i += 1
print(listOfPrimeFactors)
print(max(listOfPrimeFactors))
"""
for i in range(inp, 1, -1):
    found = False
    for j in range(2, int(sqrt(i)+1)):
        if i % j is 0:
            found = True
            break
    if found: continue
    
    print(i)
    break;
    

l = [i for i in range(inp) if i > 1]
print(l)

n = 0
while n < len(l):
    if n %2 is 0: print("currently at ",n)
    start = l[n]
    l = [item for item in l if item is start or item % start is not 0]
    n += 1


print(l)"""
