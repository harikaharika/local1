 from teacher import*
class student(teacher):
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks

i=student()
i.setname('venkey')
i.setaddress('gudur')
i.setmarks('50,40,30')
print('name=',i.getname())
print('address=',i.getaddress())
print(i.getmarks())

