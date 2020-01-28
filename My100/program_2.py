# 2. Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.

# USING FUNCTION
def fact(x):
    #x=int(x)
    if x==0:
        return 1
    else:
        return  x*fact(x-1)
x=int(input())
f=fact(x)
print(f)

#
# #USING LOOP
# x=input()
# fact=1
# x=int(x)
# if x<0:
#     print("factorial does not exist for negative numbers")
# else:
#             for i in range(1,x+1):
#                 fact=fact*i
#             print(fact)
