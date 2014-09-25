import re

eq1 = 'y = 3x + 1'#input("Enter equation1 ")
eq2 = 'y = 7x + 4'#input("Enter equation2 ")


regEx = "([1-9]*)y[\s]*=[\s]*([1-9]*)x[\s]*([+|-])[\s]*([1-9]*)[\s]*"
print(regEx)
match1 = re.search( regEx, eq1 )
match2 = re.search( regEx, eq2 )


print(match1.group(1), match1.group(2), match1.group(3), match1.group(4))
print(match2.group(1), match2.group(2), match2.group(3), match2.group(4))