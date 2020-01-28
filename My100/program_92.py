# 92. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
# after removing all duplicate values with original order reserved.

# li=[12,24,35,24,88,120,155,88,120,155]
# print(set(li))

# def removeDuplicate( li ):
list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
print(list1)


#order is not reserved
print(set(list))