
m = 2520
i = 20
while i > 2:
    #if m % 100000 is 0:
    #    print(m)
    if m % i is not 0:
        m += 1
        i = 20
    else: i -= 1
print(m)