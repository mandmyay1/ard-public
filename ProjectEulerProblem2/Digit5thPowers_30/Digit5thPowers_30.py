

def sumOfDigits(num):
    strNum = str(num)
    total = 0
    for char in strNum:
        total += int(char)**5
    if total == num: return True
    else: return False
    
#print(sumOfDigits(1634))

s = 0
start = 2
while True:
    if sumOfDigits(start):
        s += start
        print(start, s)
    start += 1