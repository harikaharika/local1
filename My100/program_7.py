# # 7. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
# # array. The element value in the i-th row and j-th column of the array should be i*j.

s=input("Enter x,y")
lis=s.split(",")
x=int(lis[0]) 
y=int(lis[1])
big_list=[]
for i in range(x):
    small_list=[]
    for j in range(y):
        small_list.append(i*j)
    big_list.append(small_list)
    print(small_list)
print(big_list)

#
# row_num = int(input("Input number of rows: "))
# col_num = int(input("Input number of columns: "))
# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
#
# for row in range(row_num):
#     for col in range(col_num):
#         multi_list[row][col]= row*col
#
# print(multi_list)
