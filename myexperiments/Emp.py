class Emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def display(self):
        print('id=%5d name=%15s sal=%.2f' %(self.id,self.name,self.sal))