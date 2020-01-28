# def palindromeRearranging(inputString):
#     for i in inputString:
#         for j in range(inputString):

# from collections import Counter
# def palindromeRearranging(inputString):
#     s = Counter(inputString)
#     odd=0
#     even=0
#     for i in s:
#         if s[i]%2==0:
#             even=even+1
#         else:
#             odd=odd+1
#      return even==len(s)or(even == len(s)-1 and odd==1)
# res=palindromeRearranging("aabb")
# print(res)


# def palindromeRearranging(inputString):
#     a=set()
#     for i in inputString:
#         if i in a:
#             a.remove(i)
#         else:
#             a.add(i)
#         return len(a) <= 1
# res=palindromeRearranging("aabbbhh")
# print(res)


# def palindromeRearranging(inputString):
#     a=set()
#     for i in inputString:
#         if i in a:
#

def palindromeRearranging(inputString):
    a=list(inputString)
    print(a)
    counter=counter[list]


