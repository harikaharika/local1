# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l4=[]
# for i in range(len(l1)):
#     l3=l1[i]+l2[i]
#     l4.append(l3)
# print(l4)


def isLucky(n):
    m = str(n)
    s = 0
    t = 0
    for i in range(int((len(m) / 2))):
        s = s + int(m[i])
    for j in range(int(len(m) / 2), len(m)):
        t = t + int(m[j])
    if s == t:
        return True
    else:
        return False
