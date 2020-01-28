# l1=[1,2,3,4,5]
# l2=[6,7,8,9]
# l=[(x1,x2)for x1 in l1 for x2 in l2]
# print(l)

# l=[1,2,3,4,5]
# l1=[]
# for x in l:
#     if x%2!=0:
#        s=x**2
#        l1.append(s)
#     else:
#         pass
#
# print(l1)

l=[1,2,3,4,5]
a=[x**2 for x in l if x%2!=0]
print(a)