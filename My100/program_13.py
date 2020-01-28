# 13. Write a program that accepts a sentence and calculate the number of letters and digits.


x=input()
d=0
l=0
for i in x:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        pass
print("Digits:",d)
print("Letters:",l)


# x=input()
# d={"DIGITS":0}
# l={"LETTERS":0}
# for i in x:
#     if i.isdigit():
#         d["DIGITS"]+=1
#     elif i.isalpha():
#         l["LETTERS"]+=1
#     else:
#         pass
# print(d["DIGITS"])
# print(l["LETTERS"])

