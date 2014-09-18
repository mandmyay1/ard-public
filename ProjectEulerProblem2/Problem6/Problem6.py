import functools
def sum_of_squares(num):
    return functools.reduce(lambda x, y: x + y, [i**2 for i in range(1, num+1)])

def square_of_sums(num):
    return (functools.reduce(lambda x, y: x + y, [i for i in range(1, num+1)]))**2

#print([i for i in range(10)])
print(sum_of_squares(100))
print(square_of_sums(100))