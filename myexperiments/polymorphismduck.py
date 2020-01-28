class duck:
    def talk(self):
        print('quak quak!')
class dog:
    def talk(self):
        print('bow bow!')
def call_talk(venkey):
    venkey.talk()
d=duck()
call_talk(d)
d=dog()
call_talk(d)

