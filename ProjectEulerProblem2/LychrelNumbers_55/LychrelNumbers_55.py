
def isPalindrome(num):
    return str(num) == str(num)[::-1]

def isLychrel(num):
    return not isLychrelIter(num, 0)

def isLychrelIter(num, currentIter):
    if currentIter > 50: return False
    strNum = str(num)
    rev = int(strNum[::-1])
    #print(strNum, strRev)
    concat = num + rev
    #print(num, rev, concat)
    if isPalindrome(concat):
        return True
    else: return isLychrelIter(concat, currentIter + 1)
    
print(isLychrel(196 ))
count = 0
for i in range(1,10000):
    if isLychrel(i): count += 1
    
print(count)