from itertools import permutations

def is_permutation(num1, num2):
    return str(num1) in [''.join(i) for i in permutations(str(num2))]

def generatePossibleNumber():
    start = 1
    x = 1
    while True:
        if int(str(x)[0]) >= 2: 
            start *= 10
            x = start
        x2 = 2*x
        if is_permutation(x, x2):
            #yield x
            x3 = 3*x
            if is_permutation(x,x3):
                x4 = 4*x
                if is_permutation(x,x4):
                    x5 = 5*x
                    if is_permutation(x,x5):
                        x6 = 6*x
                        if is_permutation(x,x6):
                            return (x,x2,x3,x4,x5,x6)
        x += 1
        #if %10000 is 0: print("at", x)

generated = generatePossibleNumber()
print(generated)
