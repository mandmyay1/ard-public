from itertools import permutations

perms = set()
for perm in permutations('123456789', 9):
    perms.add("".join(perm))

concats = []
integer = 1
while integer < 10000:
    eachof = 1
    concatenatedString = ""
    while len(concatenatedString) < 9:
        concatenatedString += str(integer *eachof)
        eachof += 1
    if len(concatenatedString) is 9:
        if concatenatedString in perms:
            concats.append(int(concatenatedString))
    integer += 1

print(len(concats), max(concats))