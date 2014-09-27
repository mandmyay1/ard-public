
def properDivisors(num):
    retList = []
    for i in range(1, num//2+1):
        if num % i is 0:
            retList.append(i)
    return retList

listAmicable = []
s = 0

for i in range(1,10000):
    possibleAmic = sum(properDivisors(i))
    if sum(properDivisors(possibleAmic)) == i and possibleAmic != i and (possibleAmic,i) not in listAmicable:
        listAmicable.append((i, possibleAmic))
        s += i + possibleAmic

if (220,284) in listAmicable:
    print("it's in there, whew")
if (284,220) in listAmicable:
    print("also in there but why not")
    
print(listAmicable)
print(s)