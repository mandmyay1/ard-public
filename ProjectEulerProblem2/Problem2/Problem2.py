
n1 = 2  #1 back
n2 = 1  #2 back
n3 = None
s = 2
for i in range(2,50):   #start at 2 because those are our base cases
    n3 = n1+n2
    if n3 > 4000000: break
    if n3 % 2 is 0: s += n3
    n2 = n1
    n1 = n3
    
print(s)