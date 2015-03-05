
def squareDigits(num):
    total = 0
    while num != 0:
        onesDigit = num %10
        num = num //10
        total += onesDigit **2
    return total

redirectsToOnes = set()
redirectsToEightyNine = set()

count89s = 0

for i in range(1,10000000):
    num = i
    while num != 1 and num != 89:
        num = squareDigits(num)
        if num in redirectsToEightyNine:
            num = 89
        elif num in redirectsToOnes:
            num = 1
        
    if num == 1:
        redirectsToOnes.add(i)
    elif num == 89:
        redirectsToEightyNine.add(i)
        count89s += 1
    
print(count89s)
#print(redirectsToEightyNine)