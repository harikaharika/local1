a=[-1, 150, 190, 170, -1, -1, 160, 180]
l1=[]
l2=[]
l4=[]
c=-1
for i in range(len(a)):
    if a[i]==-1:
        l1.append(i)
    else:
       l2.append(a[i])
       l3=sorted(l2)
for j in range(len(a)):
    if j in l1:
        l4.append(-1)
    else:
        c+=1
        l4.append(l3[c])

print(l4)