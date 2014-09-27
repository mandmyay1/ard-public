
top = 20
gmap = {(top,top):1}

def numberRoutes(currentPoint):
    global gmap
    global top# = 20
    #gridsize = (top,top)
    if currentPoint in gmap.keys(): return gmap[currentPoint]
    #if currentPoint == gridsize: return 1
    elif currentPoint[0] == top:
        num = numberRoutes((currentPoint[0], currentPoint[1]+1))
        gmap[currentPoint] = num
        return num
    elif currentPoint[1] == top: 
        num = numberRoutes((currentPoint[0]+1, currentPoint[1]))
        gmap[currentPoint] = num
        return num
    else:
        num = numberRoutes((currentPoint[0]+1, currentPoint[1])) + numberRoutes((currentPoint[0], currentPoint[1]+1))
        gmap[currentPoint] = num
        return num
    
print(numberRoutes((0,0)))