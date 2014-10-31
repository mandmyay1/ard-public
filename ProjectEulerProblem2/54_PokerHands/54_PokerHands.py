import functools

enum = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

def cmpFunc(x,y):
    if enum[x[0]] ==  enum[y[0]]: return 0
    if enum[x[0]] <  enum[y[0]]: return -1
    if enum[x[0]]>  enum[y[0]]: return 1

class hand:
    def __init__(self,inputHand):
        self.c1 = inputHand[0]
        self.c2 = inputHand[1]
        self.c3 = inputHand[2]
        self.c4 = inputHand[3]
        self.c5 = inputHand[4]
        self.listHand = inputHand
        
    def __str__(self):
        return "[" + str(self.c1) + "," + str(self.c2) + "," + str(self.c3) + "," + str(self.c4) + "," + str(self.c5) + "]"

    def getResult(self):
        return self.result

    def hasStraight(self):
        if enum[self.c2[0]] - enum[self.c1[0]] == 1:
            if enum[self.c3[0]] - enum[self.c2[0]] == 1:
                if enum[self.c4[0]] - enum[self.c3[0]] == 1:
                    if enum[self.c5[0]] - enum[self.c4[0]] == 1:
                        self.result = self.c5
                        return True
        return False
    
    def hasFlush(self):
        if self.c1[1] == self.c2[1] and self.c2[1] == self.c3[1] and self.c3[1] == self.c4[1] and self.c4[1] == self.c5[1]:
            self.result = self.c5
            return True
        return False
    
    def hasRoyalFlush(self):
        #print(hand)
        suite = self.listHand[0][1]
        if ('T',suite) in self.listHand and ('J',suite) in self.listHand and ('Q',suite) in self.listHand and ('K',suite) in self.listHand and ('A',suite) in self.listHand:
            return True
        return False
    
    def hasStraightFlush(self):
        return self.hasFlush() and self.hasStraight()
        
    def hasFourOfAKind(self):
        if self.c1[0] == self.c2[0] and self.c2[0] == self.c3[0] and self.c3[0] == self.c4[0]: 
            self.result = self.c4; 
            return True
        if self.c2[0] == self.c3[0] and self.c3[0] == self.c4[0] and self.c4[0] == self.c5[0]: 
            self.result = self.c5; 
            return True
        return False
    
    def hasFullHouse(self):
        if self.c1[0] == self.c2[0] and self.c3[0] == self.c4[0] and self.c4[0] == self.c5[0]: 
            self.result = self.c5, self.c2; 
            return True
        if self.c1[0] == self.c2[0] and self.c2[0] == self.c3[0] and self.c4[0] == self.c5[0]: 
            self.result = self.c5, self.c3; 
            return True
        return False

    def hasThreeOfAKind(self):
        if self.c1[0] == self.c2[0] and self.c2[0] == self.c3[0]: 
            self.result = self.c1
            return True
        if self.c2[0] == self.c3[0] and self.c2[0] == self.c4[0]: 
            self.result = self.c2
            return True
        if self.c3[0] == self.c4[0] and self.c4[0] == self.c5[0]: 
            self.result = self.c3
            return True
        return False

    def hasPair(self):
        if self.c1[0] == self.c2[0] or self.c1[0] == self.c3[0] or self.c1[0] == self.c4[0] or self.c1[0] == self.c5[0]: 
            self.result = self.c1
            return True
        if self.c2[0] == self.c3[0] or self.c2[0] == self.c4[0] or self.c2[0] == self.c5[0]: 
            self.result = self.c2
            return True
        if self.c3[0] == self.c4[0] or self.c3[0] == self.c5[0]: 
            self.result = self.c3
            return True
        if self.c4[0] == self.c5[0]: 
            self.result = self.c4
            return True
        
    def has2Pair(self):
        if self.c1[0] == self.c2[0]:
            if self.c3[0] == self.c4[0]: 
                self.result = self.c3,self.c1
                return True
            if self.c4[0] == self.c5[0]: 
                self.result = self.c4,self.c1
                return True
        if self.c2[0] == self.c3[0]:
            if self.c4[0] == self.c5[0]: 
                self.result = self.c4,self.c2
                return True
        return False
    
    def highestCard(self,previousHighest=None):
        if previousHighest is None:
            return self.c5
        elif previousHighest == self.c5:
            return self.c4
        elif previousHighest == self.c4:
            return self.c3
        elif previousHighest == self.c3:
            return self.c2
        elif previousHighest == self.c2:
            return self.c1
        else:
            print("HIGHEST CARD BROKEN")

def doesP1WinFromHighestCard(p1,p2):
    p1high = p1.highestCard()
    p2high = p2.highestCard()
    result = cmpFunc(p1high, p2high)
    while result == 0:
        p1high = p1.highestCard(p1high)
        p2high = p2.highestCard(p2high)
        result = cmpFunc(p1high, p2high)
    if result < 0:
        return False
    return True

def doesP1Win(p1, p2):
    if p1.hasRoyalFlush(): 
        print("p1", p1, "wins over p2 with royal straight flush", p2)
        return True
    if p2.hasRoyalFlush(): 
        print("p2", p2, "wins over p1 with royal straight flush", p1)
        return False
    if( p1.hasStraightFlush() ):
        if not p2.hasStraightFlush():
            print("p1", p1, "wins over p2 with straight flush", p2)
            return True
        p1Result = p1.getResult()
        p2Result = p2.getResult()
        if cmpFunc(p1Result, p2Result) < 0:
            print("p2", p2, "wins over p1 with straight flush high", p1)
            return False
        print("p1", p1, "wins over p2 with straight flush high", p2)
        return True
    elif p2.hasStraightFlush():
        print("p2", p2, "wins over p1 with straight flush", p1)
        return False
    
    if p1.hasFourOfAKind():
        if not p2.hasFourOfAKind():
            print("p1", p1, "wins over p2 with four-of-a-kind", p2)
            return True
        p1Result = p1.getResult()
        p2Result = p2.getResult()
        if cmpFunc(p1Result, p2Result) < 0:
            print("p2", p2, "wins over p1 with four-of-a-kind high", p1)
            return False
        print("p1", p1, "wins over p2 with four-of-a-kind high", p2)
        return True
    elif p2.hasFourOfAKind():
        print("p2", p2, "wins over p1 with four-of-a-kind", p1)
        return False
    
    if p1.hasFullHouse():
        if not p2.hasFullHouse():
            print("p1", p1, "wins over p2 with full house", p2)
            return True
        p1Result1, p1Result2 = p1.getResult()
        p2Result1, p2Result2 = p2.getResult()
        if cmpFunc(p1Result1, p2Result1) < 0:
            print("p2", p2, "wins over p1 with full house high", p1)
            return False
        print("p1", p1, "wins over p2 with full house high", p2)
        return True
    elif p2.hasFullHouse():
        print("p2", p2, "wins over p1 with full house", p1)
        return False
    
    if p1.hasFlush():
        if not p2.hasFlush():
            print("p1", p1, "wins over p2 with flush", p2)
            return True
        p1Result = p1.getResult()
        p2Result = p2.getResult()
        if cmpFunc(p1Result, p2Result) < 0:
            print("p2", p2, "wins over p1 with flush high", p1)
            return False
        print("p1", p1, "wins over p2 with flush high", p2)
        return True
    elif p2.hasFlush():
        print("p2", p2, "wins over p1 with flush", p1)
        return False
    
    if p1.hasStraight():
        if not p2.hasStraight():
            print("p1", p1, "wins over p2 with straight", p2)
            return True
        p1Result = p1.getResult()
        p2Result = p2.getResult()
        if cmpFunc(p1Result, p2Result) < 0:
            print("p2", p2, "wins over p1 with straight high", p1)
            return False
        print("p1", p1, "wins over p2 with straight high", p2)
        return True
    elif p2.hasStraight():
        print("p2", p2, "wins over p1 with straight", p1)
        return False
    
    if p1.hasThreeOfAKind():
        if not p2.hasThreeOfAKind():
            print("p1", p1, "wins over p2 with three-of-a-kind", p2)
            return True
        p1Result = p1.getResult()
        p2Result = p2.getResult()
        if cmpFunc(p1Result, p2Result) < 0:
            print("p2", p2, "wins over p1 with three-of-a-kind high", p1)
            return False
        print("p1", p1, "wins over p2 with three-of-a-kind high", p2)
        return True
    elif p2.hasThreeOfAKind():
        print("p2", p2, "wins over p1 with three-of-a-kind", p1)
        return False
    
    if p1.has2Pair():
        if not p2.has2Pair():
            print("p1", p1, "wins over p2 with two pair", p2)
            return True
        p1Result1, p1Result2 = p1.getResult()
        p2Result1, p2Result2 = p2.getResult()
        if cmpFunc(p1Result1, p2Result1) < 0:
            print("p2", p2, "wins over p1 with two pair high", p1)
            return False
        elif cmpFunc(p1Result1, p2Result1) > 0:
            print("p1", p1, "wins over p2 with two pair high", p2)
            return True
        elif cmpFunc(p1Result2, p2Result2) < 0:
            print("p2", p2, "wins over p1 with two pair high double", p1)
            return False
        print("p1", p1, "wins over p2 with two pair high double", p2)
        return True
    elif p2.has2Pair():
        print("p2", p2, "wins over p1 with two pair", p1)
        return False
    
    if p1.hasPair():
        if not p2.hasPair():
            print("p1", p1, "wins over p2 with pair", p2)
            return True
        p1Result = p1.getResult()
        p2Result = p2.getResult()
        if cmpFunc(p1Result, p2Result) < 0:
            print("p2", p2, "wins over p1 with a pair high", p1)
            return False
        elif  cmpFunc(p1Result, p2Result) > 0:
            print("p1", p1, "wins over p2 with pair high", p2)
            return True
        elif doesP1WinFromHighestCard(p1, p2):
            print("p1", p1, "wins over p2 with pair and high card", p2)
            return True
        print("p2", p2, "wins over p1 with a pair and high card", p1)
        return False
    elif p2.hasPair():
        print("p2", p2, "wins over p1 with a pair", p1)
        return False
    
    if doesP1WinFromHighestCard(p1, p2):
        print("p1", p1, "wins over p2 with a high card", p2)
        return True
    print("p2", p2, "wins over p1 with a high card", p1)
    return False


#p1 = hand([('2', 'C'),('3', 'H'),('8', 'H'),('Q', 'H'),('A', 'S')] )
#p2 = hand([('4', 'C'),('4', 'H'),('7', 'D'),('8', 'C'),('K', 'C')] )
#doesP1Win(p1, p2)


numberP1Wins = 0
file = open("p054_poker.txt")
for line in file:
    #    print(line.strip())
    cards = line.split()
    p1 = hand(sorted([(cards[i][0], cards[i][1]) for i in range(0, 5)], key=functools.cmp_to_key(cmpFunc)))
    p2 = hand(sorted([(cards[i][0], cards[i][1]) for i in range(5,10)], key=functools.cmp_to_key(cmpFunc)))
    
    if( doesP1Win(p1, p2)):
        numberP1Wins += 1
        

print(numberP1Wins)
