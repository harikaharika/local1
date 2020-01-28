# 20. Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

def putNumbers(n):
    i=0
    l=[]
    while i<n:
        j=i
        j += 1
        if j%7==0:
            yield j
        for i in range(40):
            l.append(i)
        print(l)







