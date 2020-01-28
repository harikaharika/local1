# 44. Write a program which can filter even numbers in a list by using

# filter function. The list is: [1,2,3,4,5,6,7,8,9,10].


l=[1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x: x % 2 == 0, l))
print(result)
# filter():__The filter() method filters the given sequence with the help of a
# function that tests each element in the sequence to be true or not.