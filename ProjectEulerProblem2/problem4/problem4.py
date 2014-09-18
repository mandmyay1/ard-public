
def isPalindrome(num):
    return str(num) == str(num)[::-1]

listPalindromes = []
for i in range(100,999):
    for j in range(100,999):
        if isPalindrome(i*j):
            listPalindromes.append(i*j)
            
print(listPalindromes)
print(max(listPalindromes))