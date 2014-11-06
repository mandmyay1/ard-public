

i = 1
count = 0
while True:
    for j in range(1, 1000):
        total = i**j
        if len(str(total)) == j:
            count += 1
            print(total, i,"^", j, count)
    i += 1
print(count)