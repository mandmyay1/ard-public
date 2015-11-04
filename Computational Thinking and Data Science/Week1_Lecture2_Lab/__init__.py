import random
#import numpy

mylist = []

random.seed(0)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
    print (mylist)


print 'hello'
"""
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print (mylist)

def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 
    

rand1 = [dist1() for i in range(0, 1000)]
rand2 = [dist2() for i in range(0, 1000)]

avg1 = sum(rand1)/len(rand1)
avg2 = sum(rand2)/len(rand2)

#print(avg1, avg2)


def test3():
    mylist = []
    
    for i in range(random.randint(1, 10)):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
    print(mylist)

#test3();
#test3()
random.seed()

def test4():
    mylist = []

    for i in range(random.randint(1, 10)):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            if number not in mylist:
                mylist.append(number)
    print (mylist)
    
test4()
test4()

random.seed()
def test5():
    mylist = []

    random.seed(0)
    for i in range(random.randint(1, 10)):
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
        print (mylist)
        
#test5()
test5()"""