
listAvailable = [1,2,5,10,20,50,100,200]
def numberCoins(total):
    combinations = 0
    for num in listAvailable:
        if total == num: combinations += 1
        elif total - num < 0: pass
        else: combinations += numberCoins( total - num )
    return combinations


print(numberCoins(3))