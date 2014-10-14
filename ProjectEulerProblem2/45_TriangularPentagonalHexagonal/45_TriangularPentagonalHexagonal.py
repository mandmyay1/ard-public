

def generateTriangle():
    n = 1
    while True:
        yield n*(n+1)//2
        n += 1
        
def generatePentagonal():
    n = 1
    while True:
        yield n*(3*n-1)//2
        n += 1
        
def generateHexagonal():
    n = 1
    while True:
        yield n*(2*n-1)
        n += 1
        
generateT = generateTriangle()
generateP = generatePentagonal()
generateH = generateHexagonal()

t = next(generateT)
p = next(generateP)
h = next(generateH)

#print(t, p, h)

while True:
    if t == p and t == h: print(t,p,h)
    if t == min(t,p,h):
        t = next(generateT)
    elif p == min(t,p,h):
        p = next(generateP)
    elif h == min(t,p,h):
        h = next(generateH)
