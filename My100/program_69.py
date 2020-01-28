# 69. Please write assert statements to verify that every number in the list [2,4,6,8] is even.

l=[2,4,6,8]
for i in l:
    assert i%2==0

# Assertions are simply boolean expressions that checks if the conditions return true or not.
# If it is true, the program does nothing and move to the next line of code.
# However, if it's false, the program stops and throws an error.