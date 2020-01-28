# def arrayChange(inputArray):
#     moves = 0
#
#     for i in range(len(inputArray) - 1):
#         left = inputArray[i]
#         right = inputArray[i + 1]
#         # print(left)
#         # print(right)
#
#         if left >= right:
#             tmp_moves = left - right +1
#             inputArray[i + 1] += tmp_moves
#             moves += tmp_moves
#     return moves
# res=arrayChange([1,1,1])
# print(res)


def arrayChange(l):
   c=0
   for i in range(1,len(l)):
       if l[i]<=l[i-1]:
           s=(l[i-1]-l[i])+1
           print(s)
           l[i]=l[i-1]+1
           c+=s
   return c
res=arrayChange([1,1,1])
# print(res)