
def expBySquare(x,n):
    if n < 0:
        return expBySquare(1/x, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return x
    elif n %2 == 0:
        return expBySquare(x**2, n/2)
    else:
        return x * expBySquare(x**2, (n-1)/2)

maxBase = 0
maxExponent = 0
justMax = 0
file = open("p099_base_exp.txt")
length = 0
position = 0
for line in file:
    length += 1
    splitsies = line.split(",")
    base = int(splitsies[0])
    exp = int(splitsies[1])
    if base < maxBase and exp < maxExponent: continue
    calc = base ** exp
    if calc > justMax:
        justMax = calc
        maxExponent = exp
        maxBase = base
        position = length
        print(length)

file.close()
print( maxBase, maxExponent, length)
        