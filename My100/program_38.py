# 38. Define a function which can generate a list where the values are square of numbers
# between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

def sqrlist():
    l=[]
    for i in range(1,21):
        l.append(i**2)
    return  l[-5:]
print(sqrlist())