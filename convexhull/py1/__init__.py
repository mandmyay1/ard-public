import math
from random import randint
from PIL import Image, ImageDraw, ImageOps

def distance( v1, v2 ):
    return math.sqrt( (v2[0]-v1[0]) * (v2[0]-v1[0]) + (v2[1]-v1[1]) * (v2[1]-v1[1]) )

def anglebetween( previousvertex, startvertex, possiblenextvertex ):
    a = distance( previousvertex, startvertex )
    b = distance( startvertex, possiblenextvertex )
    c = distance( possiblenextvertex, previousvertex )

    theta = math.acos((a*a + b*b - c*c)/(2*a*b))*180/math.pi
    return theta
    
def outsideangle( previousvertex, startvertex, possiblenextvertex ):
    return 360-anglebetween(previousvertex, startvertex, possiblenextvertex)

def findnextpoint( previousvertex, startvertex, allothervertices ):
    minangle = 360
    minvertex = (0,0)
    for v in allothervertices:
        angle = outsideangle(previousvertex, startvertex, v)
        if minangle > angle: minangle = angle; minvertex = v
    return minvertex

if __name__ == '__main__':
    vertices = [(randint(0,500),randint(0,500)) for _ in range(randint(50,100))]
    img = Image.new('RGB', (501,501),'black')
    draw = ImageDraw.Draw( img )
    
    hull = []
    leftmost =  min( vertices )
    startvertex = leftmost
    vertices.remove(startvertex)
    initialpreviousvertex = (startvertex[0],0)
    print( startvertex )
    hull.append( startvertex )
    nextpoint = findnextpoint( initialpreviousvertex, startvertex, vertices )
    while nextpoint is not leftmost and 0 is not len( vertices ):
        print(nextpoint)
        hull.append( nextpoint )
        vertices.append( startvertex )
        vertices.remove( nextpoint )
        initialpreviousvertex = startvertex
        startvertex = nextpoint
        nextpoint = findnextpoint( initialpreviousvertex, startvertex, vertices )
    
    draw.polygon(hull, outline='red')
    draw.point( vertices, fill='white')
    #img.thumbnail((500,500))
    img = ImageOps.flip(img)
    img.save("hull.png", 'PNG')
