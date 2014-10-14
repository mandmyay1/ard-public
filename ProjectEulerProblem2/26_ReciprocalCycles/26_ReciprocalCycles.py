
def longDivision(numerator, denominator):
    listNumerators = [numerator]
    while numerator != 0:
        for i in range(1,10):
            if i*denominator > numerator: 
                i-=1; 
                break
        numerator = numerator -i*denominator
        numerator *= 10
        if numerator in listNumerators:
            index = listNumerators.index(numerator)
            return len(listNumerators) - index
        listNumerators.append(numerator)
    return 0

longest = 0
denominatorOfLongest = 0
for i in range(1,1000):
    cycleLength = longDivision(1, i) 
    if cycleLength > longest:
        #print(cycleLength, i)
        longest = cycleLength
        denominatorOfLongest = i

#print()
print(longest, denominatorOfLongest )