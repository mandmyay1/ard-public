
def isPandigital(num):
    strNum = str(num)
    if len(strNum) != 9: return False
    for i in range(1,10):
        if str(i) not in strNum: return False
    return True

listPandigitals = []
for i in range(1,100):
    for j in range(1,10000):
        prod = i*j
        concat = str(prod)+str(i)+str(j)
        if isPandigital(int(concat)) and prod not in listPandigitals:
            print("found", i, j , prod)
            listPandigitals.append(prod)
print(listPandigitals)
print(sum(listPandigitals))
#print(isPandigital(391867254))