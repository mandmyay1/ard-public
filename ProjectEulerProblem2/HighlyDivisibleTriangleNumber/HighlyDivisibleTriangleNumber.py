import functools

def triangle_number(num):
    l = [i for i in range(1, num+1)]
    return functools.reduce(lambda x,y: x+y, l)
    
def divisors(num):
    l = []
    i = 1
    while i <= num:
        if num % i is 0: l.append(i)
        i += 1
    return l

currentTriangle = 0
i = 1
while True:
    currentTriangle = currentTriangle+i
    #print(currentTriangle)
    d = divisors(currentTriangle)
    if len(d) > 500:
        print( currentTriangle, i )
        break;
    i += 1