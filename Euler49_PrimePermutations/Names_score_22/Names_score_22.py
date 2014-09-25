


def calculateWordValue(word):
    total = 0
    for letter in word.lower():
        total += ord(letter) -96
    return total


wordsAllInOne = open("p022_names.txt")
words = []
for word in wordsAllInOne:
    wordsSeparated = word.split(',')
    for oneActualWord in wordsSeparated:
        words.append(oneActualWord.replace("\"", ""))
words = sorted(words)
print(words)

total = 0
for i in range(len(words)):
    total += ((i+1)*calculateWordValue(words[i]))
print(total)