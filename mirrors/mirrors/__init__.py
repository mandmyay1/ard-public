import sys
from math import sqrt, acos, pi, tan, atan

class mirror:
    def __init__(self, start, end):
        self.x1 = start[0]
        self.y1 = start[1]
        self.x2 = end[0]
        self.y2 = end[1]
        self.start = start
        self.end = end
    def collides(self, line):
        """ Mirror is (x1,y1,x2,y2) 
        line is (x1,y1,x2,y2, distance)"""
        m1 = slope( self.start, self.end) #slope of mirror
        m2 = slope( (line[0], line[1]), (line[2], line[3])) #slope of line
        print(m1, m2)
        xc = None
        yc = None
        if m1 is None and m2 is None: return( False, None)
        elif m1 is None: 
            yinterceptline = -m2*line[0] + line[1]
            yc = m2*(self.x1) + yinterceptline
            xc = self.x1
        elif m2 is None: 
            yinterceptmirror = -m1*self.x1 + self.y1
            yc = m1*(line[0]) + yinterceptmirror
            xc = line[0]
        else:
            yinterceptmirror = -m1*self.x1 + self.y1
            yinterceptline = -m2*line[0] + line[1]
            xc = (yinterceptline - yinterceptmirror)/(m1 - m2)
            yc = m1*xc + yinterceptmirror
        
        if m1 is m2: return (False, None)#parallel

        print( xc, yc )
        
        if between2points( self.start, self.end, (xc,yc) ): return (True, (xc,yc) )
        return (False, None)

def slope( p1, p2 ):
    if p2[0] - p1[0] == 0.0 : return None
    return (p2[1] - p1[1])/(p2[0] - p1[0])

def between( num1, num2, numtest):
    print( num1, num2, numtest)
    if numtest <= num1 and numtest >= num2: print(True); return True
    if numtest >= num1 and numtest <= num2: print(True); return True;
    print(False); return False

def between2points( p1, p2, ptest ):
    if between( p1[0], p2[0], ptest[0] ) and between( p1[1], p2[1], ptest[1] ): return True 
    else: return False

def distance(v1, v2):
    return sqrt( (v2[0]-v1[0]) **2 + (v2[1]-v1[1]) **2 )

def anglebetween( v1, v2, v3 ):
    a = distance( v1, v2 )
    b = distance( v2, v3 )
    c = distance( v3, v1 )

    theta = acos((a*a + b*b - c*c)/(2*a*b))*180/pi
    return theta

if __name__ == '__main__':
    
    #print( slope( (-1,0), (1,0) ) )
    #print( slope( (0,1), (0,-1) ) )
    numMirrors = input("Number of mirrors")
    mirrors = []
    for i in range( int(numMirrors.strip() )):
        [x1,y1,x2,y2] = sys.stdin.readline().split(" ")
        m = mirror( ( float(x1.rstrip()), float(y1.rstrip()) ) , ( float(x2.rstrip()),float(y2.rstrip()) ) )
        mirrors.append( m )
    
    line = sys.stdin.readline().split(" ")
    print( line )
    for i in range(len(line)):
        line[i] = float(line[i].rstrip())
    
    length = line[5]
    startpoint = (line[0],line[1])

    while( length > 0 ):
        minPoint = None
        angle = None
        minDistance = None
        for m in mirrors:
            (yesno,collisionpoint) = mirror.collides( m, line)
            if yesno is False: continue;
            d = distance( startpoint, collisionpoint )
            if minDistance is None or d < minDistance:
                minDistance = d
                minPoint = collisionpoint
                angle = anglebetween(startpoint, collisionpoint, m.start)
        if( length > minDistance ):
            pass
        else:
            length -= minDistance
            startpoint = collisionpoint
            newslope = tan( atan(collisionpoint[1]/collisionpoint[0]) - angle )
    print(minPoint, angle, minDistance)