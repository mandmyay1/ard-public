
def sumDivisors(num):
    s = 0
    for i in range(1,num//2+1):
        if num % i is 0:
            s += i
    return s

def isAbundant(num):
    s = sumDivisors(num)
    return s > num

listAbundants = [i for i in range(1,28124) if isAbundant(i)]

length = len(listAbundants)
setCanBeWrittenAsTwoAbundantNumbers = set()
for i in range(length):
    for j in range(i, length):
        #print("add" ,listAbundants[i]+listAbundants[j])
        sums = listAbundants[i]+listAbundants[j]
        setCanBeWrittenAsTwoAbundantNumbers.add( sums )
        

#print(len(listCanBeWritten))
#print(listCanBeWritten[0], listCanBeWritten[1])

listCantBeWritten = [i for i in range(1,28124) if i not in setCanBeWrittenAsTwoAbundantNumbers]
""""s = 0
i = 0
listindex = 0
while i < 28124:
    abundant = listCanBeWritten[listindex]
    if abundant > i:
        s += i
    elif abundant <= i:
        listindex += 1
    i += 1
    """
print(listCantBeWritten[0], listCantBeWritten[1], listCantBeWritten[len(listCantBeWritten)-1])
print(sum(listCantBeWritten))