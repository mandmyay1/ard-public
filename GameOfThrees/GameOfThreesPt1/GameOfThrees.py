
num = 31337357

while num is not 1:
    if num % 3 is 0:
        print( num, 0)
        num = num // 3
    elif (num+1)%3 is 0:
        print( num, 1)
        num = (num+1)//3
    elif (num-1)%3 is 0:
        print( num, -1)
        num = (num-1)//3
print( num )