# 87. By using list comprehension, please write a program to print the
# list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print(li)

# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
# This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

