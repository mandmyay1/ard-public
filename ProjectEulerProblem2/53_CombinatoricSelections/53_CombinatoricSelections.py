

def generateFactorial():
    start = 0
    yieldValue = 1
    yield yieldValue
    while True:
        start += 1
        yieldValue *= start
        yield yieldValue
        
dictFactorials = {}

generator = generateFactorial()
for i in range(0,101):
    fact = next(generator)
    dictFactorials[i] = fact



gt1Million = []
for n in range(1,101):
    for r in range(1, n):
        nCr = dictFactorials[n] / ( dictFactorials[r] * dictFactorials[n-r])
        if nCr > 1000000:
            gt1Million.append(nCr)

print(len(gt1Million))