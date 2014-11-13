#7830457
num = 1
for i in range(7830457):
    num *= 2
    num = int(str(num)[-10:])
print(num)

largePrime = 28433*num+1
strPrime = str(largePrime)
print( strPrime[-10:])