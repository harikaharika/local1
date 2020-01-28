# 52. Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

class Rectangle(object):
    def __init__(self,l,w):
        self.length=l
        self.width=w

    def area(self):
        return self.length*self.width

a=Rectangle(4,8)
print(a.area())