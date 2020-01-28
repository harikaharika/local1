# def check(a, b):
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             return i
# res=check([1,2,3],[1,2,3])
# print(res)

#

# def areSimilar(a,b):
#     if a==b:
#         return True
#     else:
#         return False
# res=areSimilar([1,2,3],[2,1,3])
# print(res)



# def areSimilar(a,b):
#     if a==b:
#         return True
#
#     for i in range(0, len(a)):
#         for j in range(i, len(a)):
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
#             if a==b:
#                 return True
#             a[j]=a[i]
#             a[i]=c
#
#     return False
# res=areSimilar([1,2,2],[2,1,1])
# print(res)






# # def areSimilar(a,b):
# a=[1,2,3]
# b=[2,1,3]
# l1=[]
# if a!=b:
#     if len(a)==len(b):
#         for i in range(len(a)):
#             if a[i]!=b[i]:
#                 l1.append(i)
#     else:
#         print(False)
#     if len(l1)==2 and a[l1[0]]==b[l1[1]] and a[l1[1]]==b[l1[0]]:
#         print(True)
#     else:
#         print(False)
# else:
#     print(True)
# # res=areSimilar([1, 2, 3],[2, 1, 3])
# # print(res)
# print(l1)


def areSimilar(a, b):
    l1 = []
    if a != b:
        if len(a) == len(b):
            for i in range(len(a)):
                if a[i] != b[i]:
                    l1.append(i)
        else:
            return False
        if len(l1) == 2 and a[l1[0]] == b[l1[1]] and a[l1[1]] == b[l1[0]]:
            return True
        else:
            return False
    else:
        return True
res = areSimilar([1, 2, 3], [1, 2, 3])
print(res)





