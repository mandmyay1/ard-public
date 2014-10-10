import itertools

def asciiSum(word):
    total = 0
    for ch in word:
        total += ord(ch)
    return total

file = open("p059_cipher.txt")

splitsies = list(map(lambda x: int(x), file.read().split(",")))

combs = list(itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=3))
print(len(combs))
pos = 0

needsToContain = ["that"]

for key in combs:
    output = ""
    for entry in splitsies:
        output += chr(entry ^ ord(key[pos]) )
        pos += 1
        if pos > 2: pos = 0
    for simpleWord in needsToContain:
        if simpleWord in output:
            print(asciiSum(output), output)
            break;
