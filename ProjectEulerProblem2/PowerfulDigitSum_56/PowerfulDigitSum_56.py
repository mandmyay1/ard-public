

def sumOfDigits(num):
    strNum = str(num)
    total = 0
    for char in strNum:
        total += int(char)
    return total
        
m = 0
for a in range(1,100):
    for b in range(1,100):
        s = sumOfDigits(a**b)
        if s > m: m = s
        
        
print(m)