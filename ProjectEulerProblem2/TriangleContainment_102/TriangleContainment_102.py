
def isInTriangle(A,B,C):
    (px,py) = (0,0)
    (p0x,p0y) = A
    (p1x,p1y) = B
    (p2x,p2y) = C
    Area = 1/2*(-p1y*p2x + p0y*(-p1x + p2x) + p0x*(p1y - p2y) + p1x*p2y)
    s = 1/(2*Area)*(p0y*p2x - p0x*p2y + (p2y - p0y)*px + (p0x - p2x)*py)
    t = 1/(2*Area)*(p0x*p1y - p0y*p1x + (p0y - p1y)*px + (p1x - p0x)*py)
    return s >= 0.0 and t >= 0.0 and 1-s-t >= 0.0


count = 0
f = open("p102_triangles.txt")
for line in f:
    p = line.strip().split(',')
    A = (int(p[0]),int(p[1]))
    B = (int(p[2]),int(p[3]))
    C = (int(p[4]),int(p[5]))
    if  isInTriangle(A,B,C): count += 1
    
print(count)