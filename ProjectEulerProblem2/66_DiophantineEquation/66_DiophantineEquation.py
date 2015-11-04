from math import sqrt, floor
""" x^2 - Dy^2 = 1 """

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
for i in range(2, 8):
#for i in range(151, 1001):
    print("checking", i)
    sol = minimalSolution(i)
    if sol:
        x = sol[0]
        if x > maxX:
            maxX = x
            D = sol[1]
            y = sol[2]
            print(str(x) + "x-"+str(D)+"*"+str(y)+"^2=1")
    #solutions.append(x)
#print(minimalSolution(13))
print(maxX)