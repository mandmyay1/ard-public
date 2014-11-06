from fractions import Fraction


dictionaryIterations = {}

frac1 = Fraction(1,1)
dictionaryIterations[1] = Fraction(1,2)
dictionaryIterations[2] = Fraction(1, 2 + dictionaryIterations[1])

count = 0
for n in range(2, 1001):
    fracIteration = Fraction(1, 2+ dictionaryIterations[n-1])
    dictionaryIterations[n] = fracIteration
    valueToCheck = frac1 + fracIteration
    strDen = str(valueToCheck.denominator)
    strNum = str(valueToCheck.numerator)
    if len(strNum) > len(strDen):
        count += 1
        print(n, valueToCheck);

print(count)