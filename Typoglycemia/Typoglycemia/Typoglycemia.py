import random

string = "According to a research team at Cambridge University, it doesn't matter in what order the letters in a word are, \
the only important thing is that the first and last letter be in the right place. \
The rest can be a total mess and you can still read it without a problem.\
This is because the human mind does not read every letter by itself, but the word as a whole. \
Such a condition is appropriately called Typoglycemia."

newString = ""
pointer = 0
wordStarted = True
while pointer < len(string):
    first = string[pointer]
    pointer +=1
    internals = []
    while len(string) > pointer and string[pointer] is not ' ':
        internals.append(string[pointer])
        pointer += 1
    last = ''
    if(len(internals)>1):
        last = internals[len(internals)-1]
        internals.remove(last)
    newString += first
    random.shuffle(internals)
    newString += ''.join(internals)
    newString += last
    newString += ' '
    
    pointer +=1
print(newString)