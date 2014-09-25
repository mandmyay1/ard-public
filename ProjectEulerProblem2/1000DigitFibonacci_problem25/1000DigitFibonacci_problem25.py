
def nextFibonacciNumber():
    nMinus1= 1
    nMinus2 = 1
    termNumber = 3
    while True:
        nextNumber = nMinus1 + nMinus2
        yield (nextNumber,termNumber)
        nMinus2 = nMinus1
        nMinus1 = nextNumber
        termNumber+=1
        
generator = nextFibonacciNumber()
for value in generator:
    if len(str(value[0])) >= 1000:
        print(value[1], value[0])
        break