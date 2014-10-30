from itertools import product

listAvailable = [1,2,5,10,20,50,100,200]
def numberCoins(total):
    combinations = 0
    for num in listAvailable:
        if total == num: combinations += 1
        elif total - num < 0: pass
        else: combinations += numberCoins( total - num )
    return combinations

print(numberCoins(3))

for i in range(len(listAvailable)):
    coin = listAvailable[i]
    s = [coin]
    while sum(s) < 200:
        for j in range(i,len(listAvailable)):
            pass
    
"""
setCombs = set()
for i in range(1,201):
    currentCombs = list(filter(lambda x: sum(x) == 200, product(listAvailable, repeat=i)))
    for comb in currentCombs:
        setCombs.add(tuple(sorted(list(comb))))
    
print(len(setCombs))"""