class A:
    def display(self):
        print('class A')
class B(A):
    def display(self):
        print('class B')
c=B()
c.display()