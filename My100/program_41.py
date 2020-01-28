# 41. With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the
# first half values in one line and the last half values in one line.

def halfval():
    fl=[]
    sl=[]
    tup=(1,2,3,4,5,6,7,8,9,10)
    l=len(tup)/2
    for i in range(1,int((l)+1)):
        fl.append(i)
    for j in range(int(l+1),int(len(tup)+1)):
        sl.append(j)
    print(fl)
    print(sl)
halfval()
