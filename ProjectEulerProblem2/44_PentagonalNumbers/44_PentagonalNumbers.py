


def generatePentagonal():
    n = 1
    while True:
        yield n*(3*n-1)//2
        n += 1
        
generator = generatePentagonal()

#listPentagonals = [next(generator) for _ in range(20000)]
listPentagonals = [next(generator) for _ in range(2)]
#print(listPentagonals)
while True:
    top = next(generator)
    #top = listPentagonals[n]
    for mid in listPentagonals:
        bottom = top - mid
        superBottom = mid - bottom
        if superBottom > 0 and bottom in listPentagonals and superBottom in listPentagonals:
            print( superBottom, bottom, mid, top)
    listPentagonals.append(top)
"""
for i in range(len(listPentagonals)):
    for j in range(i, len(listPentagonals)):
        diff = listPentagonals[j] - listPentagonals[i]
        summ = listPentagonals[j] + listPentagonals[i]
        if diff in listPentagonals and summ in listPentagonals:
            print(listPentagonals[j], listPentagonals[i], diff, summ)
"""
