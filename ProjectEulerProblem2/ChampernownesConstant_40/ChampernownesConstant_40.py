

def nextDigit():
    start = 1
    while True:
        yield str(start)
        start += 1
        
        
primeGenerator = nextDigit()
initial = ""
#for i in range(0,15):
for i in range(0,1000000):
    initial += next(primeGenerator)
    
mult = int(initial[0])*int(initial[9])*int(initial[99])*int(initial[999])*int(initial[9999])*int(initial[99999])*int(initial[999999])
print(mult)