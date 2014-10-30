
listAvailable = [1,2,5,10,20,50,100,200]
def changes(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]
 
print (changes(200, listAvailable))
#print changes(100000, [1, 5, 10, 25, 50, 100])
