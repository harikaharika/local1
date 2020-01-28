# 3. With a given integral number n, write a program to generate a dictionary that
# contains (i, i*i) such that is an integral number between 1 and n
# (both included). and then the program should print the dictionary.

# def dictionary(x):
#     x=input("Enter number")
#     d={}
#     x=int(x)
#     for i in range(1,x+1):
#         d[i]=i*i
#     print(d)


#USING FUNCTION
x=input("enter number")
def dictionary(x):
    d={}
    x=int(x)
    for i in range(1,x+1):
        d[i]=i*i
    print(d)
dictionary(x)
