class bank:
    def __init__(self):
        self.accno=1405
        self.name='harika'
        self.id=4564
        self.bal=10000
        self.__loan=4434
    def venkey(self):
       print('accno=',self.accno)
       print('name=',self.name)
       print('id=',self.id)
       print('bal=', self.bal)
i=bank()
i.venkey()
print(i._bank__loan)

