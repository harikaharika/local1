# 30. Define a function that can accept two strings as input and print the string with
# maximum length in console. If two strings have the same length, then the function
# should print al l strings line by line.

def lenfunc(s1,s2):
    if len(s1)>len(s2):
        return(s1)
    elif len(s2)>len(s1):
        return(s2)
    else:
        print(s1)
        print(s2)

print(lenfunc("ravi kiran","raghu"))