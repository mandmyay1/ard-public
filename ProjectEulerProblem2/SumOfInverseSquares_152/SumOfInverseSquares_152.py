from fractions import Fraction

def divideThatShit(frac, listNums):
    #print("frac", frac, "listNums", listNums)
    listReturn = []
    for number in listNums:
        #print("frac", frac, "listNums", listNums, "number", number)
        f = Fraction(1,number**2)
        if f == frac:
            #listReturn.append(number)
            return [number]
        elif f > frac:
            return None
        else:
            listNum2 = [item for item in listNums]
            listNum2.remove(number)
            listReturn = divideThatShit(frac - f, listNum2)
            if listReturn is None: continue
            listReturn.append(number)
            #print(frac, listReturn)
            return listReturn
    #print(frac, listReturn)

#listAvailableNumbers = [6,2,3,4,5,7,12,15,20,28,35]
listAvailableNumbers = [i for i in range(2,36)]
#listAvailableNumbers = [i for i in range(1,81)]
print(listAvailableNumbers)

f = Fraction(1,2)
print(f)
print(divideThatShit(f, listAvailableNumbers))
