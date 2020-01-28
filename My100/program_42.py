# 42. Write a program to generate and print another tuple whose values are even
# numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

def eventup():
    tup=(1,2,3,4,5,6,7,8,9,10)
    l=[]
    for i in tup:
        if i%2==0:
            l.append(i)
    return l
print(eventup())
