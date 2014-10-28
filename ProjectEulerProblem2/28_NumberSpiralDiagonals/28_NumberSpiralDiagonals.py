

sizeOfSpiral = 1001
sizeSquare = sizeOfSpiral **2
startat = 1

movingUp = (0,1)
movingDown = (0,-1)
movingRight = (1,0)
movingLeft = (-1,0)

initialDirection = movingRight

ourSpiral = {}
x = 0
y = 0
while startat <= sizeSquare:
    initialLocation = (x,y)
    ourSpiral[initialLocation] = startat
    startat += 1
    x += initialDirection[0]
    y += initialDirection[1]
    if initialDirection is movingRight and not (x,y-1) in ourSpiral:
        initialDirection = movingDown
    elif initialDirection is movingDown and not (x-1,y) in ourSpiral:
        initialDirection = movingLeft
    elif initialDirection is movingLeft and not (x,y+1) in ourSpiral:
        initialDirection = movingUp
    elif initialDirection is movingUp and not (x+1,y) in ourSpiral:
        initialDirection = movingRight
    
sums = ourSpiral[(0,0)]
for i in range(1,sizeOfSpiral//2+1):
    sum1=ourSpiral[(i,i)]
    sum2=ourSpiral[(-i,i)]
    sum3=ourSpiral[(i,-i)]
    sum4=ourSpiral[(-i,-i)]
    sums += sum1 + sum2 + sum3 + sum4
    print(sum1, sum2, sum3, sum4, sums)


print(sums)