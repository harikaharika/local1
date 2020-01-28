# 48. Write a program which can map() to make a list whose elements are
# square of numbers between 1 and 20 (both included).

sqrnum=list(map(lambda x : x**2, range(1,21)))
print(sqrnum)