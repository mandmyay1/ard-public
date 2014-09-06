from random import shuffle
import sys


inputs = sys.stdin.readline().split(" ")
input1 = inputs[0]
input2 = inputs[1].rstrip()
count = 0;
while input1 != input2:
    input1 = list(input1)
    shuffle(input1)
    input1=''.join(input1)
    count += 1
    
print(count)