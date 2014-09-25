
def fact(n):
    start = 1
    mult = 1
    while mult <= n:
        start *= mult
        mult += 1
    return start

def f(n):
    total = 0
    for char in str(n):
        total += fact(int(char))
    return total

def sf(n):
    fn = f(n)
    total = 0
    for char in str(fn):
        total += int(char)
    return total

def g(i):
    start = 1
    while True:
        sfs = sf(start)
        if sfs is i:
            return start
        start += 1

def sg(i):
    gi = g(i)
    total = 0
    for char in str(gi):
        total += int(char)
    return total
    
#print(fact(1))
#print(fact(2))
#print(fact(5))
#print(f(342))
#print(sf(342))
#print(g(5))
#print(sg(5))
#print(g(20))
#print(g(1))
#print(sg(1))
#for i in range(1,41):
#    print(g(i))
    

t = 0
for i in range(1, 21):
    t += sg(i)
    #print(i, t)
print(t)

t = 0
for i in range(1, 150):
    t += sg(i)
    print(i, t)
print(t)
