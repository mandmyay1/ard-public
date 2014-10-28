from fractions import Fraction

def canCancelDigits(numerator, denominator):
    ref = Fraction(numerator,denominator)
    strNum = str(numerator)
    strDen = str(denominator)
    if strNum[0] == strDen[0]:
        if ref == Fraction(int(strNum[1]),int(strDen[1])): return True
    elif strNum[0] == strDen[1]:
        if ref == Fraction(int(strNum[1]),int(strDen[0])): return True
    elif strNum[1] == strDen[0]:
        if ref == Fraction(int(strNum[0]),int(strDen[1])): return True
    elif strNum[1] == strDen[1]:
        if ref == Fraction(int(strNum[0]),int(strDen[0])): return True
    return False

listDigitCancelers = []
for i in range(10,100):
    for j in range(10,100):
        if i %10 == 0 or j %10 == 0: continue
        if canCancelDigits(i, j) and i/j < 1.0:
            print("adding",i,j)
            listDigitCancelers.append(Fraction(i,j))

print(listDigitCancelers)
mult = Fraction(1,1)
for digit in listDigitCancelers:
    mult = mult * digit
print(mult)