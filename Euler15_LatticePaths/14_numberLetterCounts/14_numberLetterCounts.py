

listWords = []
oneToNine = ['', 'one','two','three','four','five','six','seven','eight','nine', 'ten']
teens = 'eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
for i in range(0, 10):
    prefix = ''
    if i is not 0:
        prefix = oneToNine[i] + ' hundred and '
        listWords.append( oneToNine[i] + ' hundred')
    for num in range(1,11):
        listWords.append(prefix + oneToNine[num])
    listWords.extend([prefix + teen for teen in teens])
    for w in 'twenty thirty forty fifty sixty seventy eighty ninety'.split():
        #print(w)
        for i in range(0,10):
            #print(oneToNine[i])
            listWords.append(prefix + w + oneToNine[i])
listWords.append('one thousand')

count = 0
for i in listWords:
    print(i.replace(' ', ''))
    count += len(i.replace(' ', ''))
    
print(count)