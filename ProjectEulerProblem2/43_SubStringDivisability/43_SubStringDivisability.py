from itertools import permutations

perms = list(permutations('0123456789', 10))
#print(len(perms), perms[0], perms[1], perms[len(perms)-1])
runningSum = 0
for perm in perms:
    stringPerm = "".join(perm)
    if int(stringPerm[7:10]) % 17 is 0:
        #print(stringPerm, 17)
        if int(stringPerm[6:9]) % 13 is 0:
            #print(stringPerm, 13)
            if int(stringPerm[5:8]) % 11 is 0:
                if int(stringPerm[4:7]) % 7 is 0:
                    if int(stringPerm[3:6]) % 5 is 0:
                        if int(stringPerm[2:5]) % 3 is 0:
                            if int(stringPerm[1:4]) % 2 is 0:
                                runningSum += int(stringPerm)
                                print("ahhh found one", stringPerm, runningSum)
                                
print(runningSum)