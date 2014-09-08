from random import shuffle
from sys import stdin


if __name__ == '__main__':
    numdex = int( stdin.readline().strip() )
    blackjacks = 0
    rounds = 0
    for j in range(10000):
        deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]*4*numdex
        shuffle(deck)
        while len(deck) > 3:
            c1 = deck.pop(0)
            c2 = deck.pop(0)
            s = c1+c2
            rounds +=1
            if c2 == 11 or c1 == 11: 
                if 21 == c2+c1: blackjacks+=1
                continue
            while s <= 11:
                c3 = deck.pop();
                s += c3
                if c3 == 11: 
                    if 21 == s: blackjacks+=1
            
    print( blackjacks, rounds )
    print( blackjacks/rounds * 100)