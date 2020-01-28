# 64. Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
# with a given n input by console (n>0).

n=input()
n=int(n)
def f(n):
    if n==0:
        return 1
    else:
        return f(n-1)+100
print(f(n))