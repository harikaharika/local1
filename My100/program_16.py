# # 16. Use a list comprehension to square each odd number in a list.
# # The list is input by a sequence of comma-separated numbers.

list=[2,3,4,5,7,9]
list1=[i**2 for i in list if i%2!=0 ]
print(list1)

# x=input('')
# squares=[]
# # values=x.split(',')
# # k=int(list[values])
# # for i in values:
# #     if int(i)%2!=0:
# #         squares.append(int(i)*int(i))
# #     else:
# #         pass
# # print(squares)
#
# sr=[int(i)**2 for i in x.split() if int(i)%2!=0]
# print(sr)
#
# # l=([i*2 for i in range(0,100) if i%2==0])
# # print(l)


# a=(i for i in range(0,10))
# print(a)
# a=['a','b','c']
# b=[1,2,3]
# dict1={a:a*2 for a in [1,2,3,4]}
# print(dict1)


# k=[1,2,3,4]
# s=('a','b','c')
# dict2 = {s:k for (s,k) in zip(s,k)}
# print(dict2)



