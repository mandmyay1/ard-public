"""How many of the words in words.txt are triangle words?"""

def generateNextTriangle():
    i = 1
    start = 0
    while True:
        start += i
        yield start
        i += 1

def calculateWordValue(word):
    total = 0
    for letter in word.lower():
        total += ord(letter) -96
    return total

triangleWords = []
triangleNumbers = []
gen = generateNextTriangle()
triangleNumbers.append(next(gen))

wordsAllInOne = open("words.txt")
words = []
for word in wordsAllInOne:
    wordsSeparated = word.split(',')
    for oneActualWord in wordsSeparated:
        words.append(oneActualWord.replace("\"", ""))
print(words)

for word in words:
    v = calculateWordValue(word)
    while v > max(triangleNumbers):
        triangleNumbers.append(next(gen))
    if v in triangleNumbers:
        triangleWords.append(word)
print ('SKY' in triangleWords)
print( len(triangleWords))