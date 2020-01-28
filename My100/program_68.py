# 68. Please write a program using generator to print the numbers which can be
# divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

x=int(input())
l=[]
def generatorfunc(x):
    for i in range(x):
        if i%5==0 and i%7==0:
            yield i
for i in generatorfunc(x):
    l.append(i)
print(l)

