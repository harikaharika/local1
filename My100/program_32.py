# 32. Define a function which can print a dictionary where the keys are numbers
# between 1 and 3 (both included) and the values are square of keys.


# def squaresdict():
#     d=dict()
#     l=[]
#     for i in range(1,4):
#         d[i]=i**2
#     return d
# squaresdict()

def sqrdict():
    d={}
    for i in range(1,4):
        d[i]=i*i
        i+=1
    return d
print(sqrdict())