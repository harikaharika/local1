# 12. Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.The numbers obtained should be
# printed in a comma-separated sequence on a single line.


l = ['0','2','4','6','8']
for i in range(1000,5000):
    for j in str(i):
        if j not in l:
            break
    else:
         print(i)


# for i in range(1000,5000):
#     for j in str(i):
#         if int(j)%2!=0:
#             break
#     else:
#          print(i)


# values=[]
# for i in range (2000,2010):
#     s=str(i)
#     if(int(s[0])%2==0)and(int(s[1])%2==0)and(int(s[2])%2==0)and(int(s[3])%2==0):
#         values.append(s)
# print(",".join(values))


#*
# l = []
# for i in range(2000,3000):
#     x = str(i)
#     if int(x)%2 == 0:
#         l.append(x)
# print(','.join(l))