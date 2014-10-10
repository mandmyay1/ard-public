

#myList = []
myDict = {}
file = open("p067_triangle.txt")
i = 0
for line in file:
    splitsies = line.split()
    for j in range(len(splitsies)):
        myDict[(i,j)] = int(splitsies[j])
#        myList.append({(i,j):int(splitsies[j])})
    i+=1
    
i-=1
print(myDict)
print(i)
for entry in reversed(sorted(myDict)):
    if entry[0] == i: continue
    possibleSpot1 = (entry[0]+1, entry[1])
    possibleSpot2 = (entry[0]+1, entry[1]+1)
    possibleSum1 = myDict[entry] + myDict[possibleSpot1]
    possibleSum2 = myDict[entry] + myDict[possibleSpot2]
    myDict[entry] = max(possibleSum1, possibleSum2)
    print(entry, myDict[entry])

print(myDict[(0,0)])