# factorial = 1
#
# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)

# n=5
# fact=1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
res=fact(5)
print(res)