# 11.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
# input and then check whether they are divisible by 5 or not. The numbers that are divisible
# by 5 are to be printed in a comma separated sequence.


l=[]
x=input()
items=x.split(',')
for p in items:
    q=int(p)
    if q%5==0:
        l.append(p)
print(','.join(l))


# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if intp%5!=0:
#         value.append(p)
#
# print(','.join(value))