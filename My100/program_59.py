# 59.Write a program which accepts a sequence of words separated by
# whitespace as input to print the words composed of digits only.

x=input()
l=[]
lis=[l.append(word) for word in x.split() if word.isdigit()]
print(l)

# w=x.split(" ")
# l=[]
# for word in w:
#     if word.isdigit():
#         l.append(word)
#     else:
#         pass
#print(l)