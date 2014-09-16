from random import randint

def lookNSay(number, seed=1):
    if number is 1: return seed
    strNum = str(lookNSay(number-1, seed))
    strReturn = ''
    count = 0
    prevchar = strNum[0]
    for c in strNum:
        if c is prevchar: count += 1
        else:
            strReturn += str(count) + prevchar
            count = 1
        prevchar = c
    strReturn += str(count) + prevchar
    return int(strReturn)

#num = int(input("Enter positive number, sequence number "))
seed = randint(1,500)
num = randint(30,40)
print("lookNSay", num, seed)
print(lookNSay(num, seed))