import math


def finda0(n):
    start = 1
    while True:
        if (start+1) **2 <= n:
            start +=1
        else: break
    return start


def sqrt(n):
    order = []
    repeating = []
    mn = 0
    dn = 1
    an = finda0(n)
    a0 = an
    if a0**2 == n: return False
    order.append((an, mn, dn))
    
    while True:
        mn1 = dn*an-mn
        dn1 = (n - mn1**2)//dn
        an1 = math.floor( (a0 + mn1) // dn1 )
        combo = (an1, mn1, dn1)
        if combo in order:
            #print( repeating )
            if len(repeating) %2 == 1: return True
            else: return False
            
        order.append(combo)
        repeating.append(an1)
        an = an1
        dn = dn1
        mn = mn1

count = 0
for i in range(2, 10001):
    if sqrt(i):
        count+=1
print(count)