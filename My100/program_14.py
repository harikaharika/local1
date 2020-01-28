# 14. Write a program that accepts a sentence and calculate the number of upper case letters and
# lower case letters.

x=input()
u=0
l=0
for i in x:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    else:
        pass
print("Upper:",u)
print("Lower:",l)
