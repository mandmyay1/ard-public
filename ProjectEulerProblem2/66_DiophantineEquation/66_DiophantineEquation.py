from math import sqrt, floor
""" x^2 - Dy^2 = 1 """

highestD = 1000

solutions = {}
maxD = set([i for i in range(1,highestD+1)])
removeThese = []
for D in maxD:
    sqrtD = sqrt(D)
    if sqrtD == floor(sqrtD):
        removeThese.append(D)
for item in removeThese:
    maxD.remove(item)
    
squares = set()
maxKey = 0
maxSquare = 0

def generateSquares():
    global squares
    global maxKey
    global maxSquare
    start = 1
    while True:
        maxSquare = start **2
        squares.add(maxSquare)
        start += 1
        yield maxSquare

squareGenerator = generateSquares()

#Generate squares up to num
def genSquares(num):
    while num > maxKey:
        next(squareGenerator)

#genSquares(100)
maxX = 0
DatMaxX = 0
xsq = next(squareGenerator)
while len(maxD) > 0:
    removeThese = []
    for D in maxD:
        ysq = (xsq - 1)/ D
        if ysq == floor(ysq):
            ysq = int(ysq)
            if ysq in squares:
                solutions[D] = sqrt(xsq)
                x = solutions[D]
                y = sqrt(ysq)
                if x > maxX:
                    maxX = solutions[D]
                    DatMaxX = D
                removeThese.append(D)
                print( str(x) + "x-"+str(D)+"*"+str(y)+"^2=1")
    for item in removeThese:
        maxD.remove(item)
    xsq = next(squareGenerator)
print(maxX, DatMaxX)

"""def minimalSolution(D):
    sqrtD = sqrt(D)
    if sqrtD == floor(sqrtD):
        return None
    y = 1
    while True:
        #if y >= maxKey:
        #    genSquares(y)
        ySide = 1+D*squares[y]
        genSquares(ySide)
        if ySide in squaresAsKeys:
            x = squaresAsKeys[ySide]
            return (x, D, y)
        y+=1
"""
#minimalSolution(5)
#minimalSolution(13)
"""
def minimalSolution(D):
    sqrtD = sqrt(D)
    if sqrtD == floor(sqrtD):
        return None
    y = 1
    x = None
    while True:
        yside = 1 + D*y**2
        x = sqrt( yside )
        xfloor = floor(x)
        if x == xfloor and xfloor**2 == yside:
            return (x, D, y)
            #return str(x) + "x-"+str(D)+"*"+str(y)+"^2=1"
        y+=1
        

#print(minimalSolution(2))
#solutions = []
maxX = 0
DatMaxX = 0
#for i in range(2, 8):
for i in range(151, 1001):
    print("checking", i)
    sol = minimalSolution(i)
    if sol:
        x = sol[0]
        if x > maxX:
            maxX = x
            DatMaxX = sol[1]
            y = sol[2]
            print(str(x) + "x-"+str(DatMaxX)+"*"+str(y)+"^2=1")
    #solutions.append(x)
#print(minimalSolution(13))
print(maxX)"""