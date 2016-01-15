
num = 18446744073709551614

possibleChoices = [-2, -1, 0, 1, 2]

def trySolution(num, stack):
    if num is 1:
        addBits = [item[1] for item in stack]
        if sum(addBits) is 0:
            for item in stack:
                print( item[0], item[1] )
            print(num)
            print( addBits )
            return True
        return False
    elif num is 0:
        return False
    validChoices = [choice for choice in possibleChoices if (num+choice)%3 is 0]
    for choice in validChoices:
        copyStack = list(stack)
        copyStack.append((num, choice))
        if trySolution((num+choice)//3, copyStack):
            return True
    return False
if not trySolution(num, []):
    print("Impossible")
    
