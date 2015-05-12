def triangle(n): return n*(n+1)//2
def square(n): return n**2
def pentagonal(n): return n*(3*n-1)//2
def hexagonal(n): return n*(2*n-1)
def heptagonal(n): return n*(5*n-3)//2
def octagonal(n): return n*(3*n-2)

def generateTheseThings(func):
    ret = set()
    i = 1
    t = func(i)
    while t < 10000:
        if t >= 1000:
            ret.add(t)
        i += 1
        t = func(i)
    return ret

def generateSequence( listOfFigurates ):
    lastFigurate = listOfFigurates.pop()
    for i in lastFigurate:
        sequence = generateNextSequence(listOfFigurates, [i]);

def generateNextSequence( listOfFigurates, sequence ):
    nextList = list(listOfFigurates)
    if len(nextList) == 0:
        print(sequence)
        print(sum(sequence))
        return True
    lastNumberInSequence = str(sequence[len(sequence)-1])
    last2Chars = lastNumberInSequence[2:]
    if last2Chars[0] == '0':
        return False
    first2CharsInSequence = str(sequence[0])[:2]
    matchFirstAsWell = False
    if len(sequence) == 5:
        matchFirstAsWell = True
    for i in range(len(nextList)):
        figurate = nextList.pop(i)
        for j in figurate:
            first2Chars = str(j)[:2]
            if matchFirstAsWell:
                seriouslyLast2Chars = str(j)[2:]
                if seriouslyLast2Chars != first2CharsInSequence: continue
            if first2Chars == last2Chars and j not in sequence:
                sequenceCopy = list(sequence)
                sequenceCopy.append(j)
                success = generateNextSequence( nextList, sequenceCopy )
                if success:
                    return success
        nextList.insert(i, figurate)
    return False

triangles = generateTheseThings(triangle)
squares = generateTheseThings(square)
pentagonals = generateTheseThings(pentagonal)
hexagonals = generateTheseThings(hexagonal)
heptagonals = generateTheseThings(heptagonal)
octagonals = generateTheseThings(octagonal)

figurates = [triangles, squares, pentagonals, hexagonals, heptagonals, octagonals]
generateSequence(figurates)


