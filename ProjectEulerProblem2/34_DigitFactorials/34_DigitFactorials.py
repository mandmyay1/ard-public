

def fact(n):
    if n == 0: return 1
    return n * fact(n-1)

def isDigitFactorial(num):
    strNum = str(num)
    s = sum([ fact(int(ch)) for ch in strNum ])
    return s == num

digitFacts = [i for i in range(3,1000000) if isDigitFactorial(i)]

print(digitFacts)