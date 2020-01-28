# 67. Please write a program using generator to print the even numbers
# between 0 and n in comma separated form while n is input by console.

x=int(input())
l=[]
def generatoreven(x):
    i=0
    while i<=x:
        if i%2==0:
            yield i
        i+=1
for i in generatoreven(x):
    l.append(i)
print(l)



