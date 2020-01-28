# 63. Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

x=input()
sum=0
for i in range(1,int(x)+1):
    i=float(i)
    sum += float(i/(i+1))
print(sum)