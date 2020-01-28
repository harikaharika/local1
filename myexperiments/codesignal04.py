# 4.Given an array of integers,
# find the pair of adjacent elements that has the largest product and return that product.

def adjacentElementsProduct(inputArray):
    pro = inputArray[0]
    product = pro * inputArray[1]
    for i in inputArray[1:]:
        if pro * i > product:
            product = pro * i
        pro = i
    return product
print(adjacentElementsProduct([3,6,-2,-5,7,3]))