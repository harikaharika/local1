# Python Program to Check a Given String is Palindrome or Not.
# str=input("Please enter your own str: ")
# if(str==str[::-1]):
#    print("It is a Palindrome str")
# else:
#    print("It is Not a Palindrome str")


def palin(str):
    if(str==str[::-1]):
        return "It is a palindrome string"
    else:
        return "It is not a palindrome string"

s=input("please enter your own string:")
res=palin(s)
print(res)