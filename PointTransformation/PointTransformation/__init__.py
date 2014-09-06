from math import cos, sin, pi, sqrt

class Transformer:
    def __init__(self, initialpoint):
        (self.x,self.y) = (initialpoint[0],initialpoint[1])
                              
    def translate(self, translation):
        (self.x,self.y) = (self.x + translation[0],self.y + translation[1])
    
    def rotateclockwise(self, around, radians ):
        Transformer.rotate( self, around, - radians )
    
    def rotate(self, around, radians):
        (x,y) = (self.x-around[0],self.y-around[1])
        self.x = x*cos(radians)-y*sin(radians) + around[0]
        self.y = x*sin(radians)+y*cos(radians) + around[1]
    
    def scale(self, around, factor):
        (x,y) = (self.x-around[0],self.y-around[1])
        (self.x,self.y) = (factor * x + around[0], factor * y + around[1])
    
    def reflect(self, axis):
        if axis is 'X': self.y *= -1
        elif axis is 'Y': self.x *= -1
    
    def distance(self, end):
        return sqrt( ( self.x - end[0] )**2 + ( self.y - end[1] )**2 )
    
    def finish(self):
        print( self.x, self.y)
#(strx,stry) = input("Enter initial point ").strip(")").strip("(").split(",")
#x,y = float(strx),float(stry)
#(x,y) = (2.0,5.0)
#around = (3.0,2.0)
#theta = pi/2
#print(x,y)
#print( rotateclockwise( (x,y) , around, theta ) )
#print( rotateclockwise( (x,y) , around, pi ) )
#print( translate( (x,y) , around ) )
#print( scale( (x,y), around, 3) )
#print( "__________________")

t = Transformer( (0,5) )
t.translate( (3,2) )
t.scale( (1,3), .5 )
t.rotateclockwise((3,2), 1.57079632679 )
t.reflect( 'X' )
t.translate( (2,-1) )
t.scale( (0,0),-0.25)
t.rotateclockwise( (1,-3), 3.14159265359 )
t.reflect( 'Y' )
t.finish()