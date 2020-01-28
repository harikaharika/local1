# 31. Define a function that can accept an integer number as input and print "It is an even number"
# if the number is even, otherwise print "It is an odd number".

def evenum(x):
    if x%2==0:
        return "It is an even number"
    else:
        return "It is an odd number"
print(evenum(6))