"""N-Sad Cycles. Take a number, raise it's digits to a certain power (base), add those up, they're the next number.
Eventually the numbers will repeat. Print out the repeating numbers
 """
base = 11
number = 2
sadCycle = []

def nextCycleElement(b, n):
    strN = str(n)
    total = 0
    for ch in strN:
        total += int(ch) ** b
    return total

while sadCycle.count(number) == 0:
    sadCycle.append(number)
    number = nextCycleElement(base, number)

print(sadCycle[sadCycle.index(number):])