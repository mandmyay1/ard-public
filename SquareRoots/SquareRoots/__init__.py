from decimal import *
import functools
squareOf = 2#int(input("Enter number to find square root of "))
digitsPrecision = 100000#int(input("Enter number of digits of precision "))
getcontext().prec = digitsPrecision
oldterm = 0.0
nextTerm = squareOf //2
while(nextTerm != oldterm):
    oldterm = nextTerm
    nextTerm = Decimal(1/2)*(oldterm + Decimal(squareOf)/Decimal(oldterm))
    
content = []
with open("incorrectsquareroot.txt") as content_file:
    content = content_file.read()
incorrectStr = functools.reduce(lambda x,y: x.strip()+y.strip(), content)
strCorrect = str(nextTerm)
for i in range( min( len(strCorrect), len(incorrectStr) ) ):
    if strCorrect[i] != incorrectStr[i]:
        print("Found invalid number", incorrectStr[i], "(Should be", strCorrect[i], ")at position", i)
