

def factorial():
    start = 1
    n = 1
    while True:
        start = start * n
        yield start
        n += 1
        
generator = factorial()
for _ in range(1,100):
    next(generator)
    
fact100 = str(next(generator))
total = 0
for char in fact100:
    total += int(char)
print(total)