from math import sqrt

def distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return sqrt( (float(x2)-float(x1))**2 + (float(y2)-float(y1))**2 )

file = open("sample3.txt")

points = [line.split() for line in file]

totalDistance = 0.0
currentPoint = (.5,.5)
while len(points) > 0:
    #find closest point
    minDistance = -1
    pointToRemove = None
    for p in points:
        dist = distance( currentPoint, p )
        if minDistance == -1 or dist < minDistance:
            minDistance = dist
            pointToRemove = p
    totalDistance += minDistance
    nx,ny = pointToRemove
    currentPoint = (float(nx), float(ny))
    points.remove(pointToRemove)

print(totalDistance)