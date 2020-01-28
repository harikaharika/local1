# 66. The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program using list comprehension to print the Fibonacci Sequence
# in comma separated form with a given n input by console.


n=int(input())
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))
