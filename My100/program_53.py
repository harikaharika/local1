# 53. Define a class named Shape and its subclass Square. The Square class has an
# init function which takes a length as argument. Both classes have a area function
# which can print the area of the shape where Shape's area is 0 by default.

class Shape():
    def __init__(self):
        pass
    def shapearea(self):
        return 0

class Square(Shape):
    def __init__(self,l):
        self.length=l
    def squarearea(self):
        return self.length*self.length

print(Square(4).squarearea())
print(Shape().shapearea())