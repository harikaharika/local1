# 94. Please write a program which count and print the numbers of each character in a string input by console.

dic = {}
s=input()
for i in s:
    dic[i] = dic.get(i,0)+1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))