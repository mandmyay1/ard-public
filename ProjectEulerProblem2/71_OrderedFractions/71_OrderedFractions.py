from fractions import Fraction
import math

closest = 0
closestTo = Fraction(3,7)
difference = 1

"""This will be within the last 1000 or so, so don't bother checking the first 999,000"""
for d in range(1000001, 999000, -1):
    n = math.floor(closestTo * d)
    f = Fraction(n,d)
    
    if closestTo - f < difference and f != Fraction(3,7):
        closest = f
        difference = closestTo-f

print(closest)