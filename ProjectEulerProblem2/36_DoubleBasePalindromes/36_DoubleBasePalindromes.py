

def isPalindrome(num):
    return str(num) == str(num)[::-1]

runningSum = 0
for x in range(1000000):
    binary = bin(x)[2:]
    if isPalindrome(str(x)) and isPalindrome(binary):
        runningSum += x
        
print( runningSum )