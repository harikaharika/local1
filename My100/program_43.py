# 43. Write a program which accepts a string as input to print "Yes"
# if the string is "yes" or "YES" or "Yes", otherwise print "No".

def strlogical():
    s=input()
    if s =="Yes" or s=="yes" or s=="YES":
        return "Yes"
    else:
        return "No"
print(strlogical())