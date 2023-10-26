class Phone:
    def __init__(self,number,model,weight):
        self.number = number
        self.model = model
        self.weight = weight

    def Rd(self):
        print(self.model, self.number, self.weight)
    def receiveCall(self,name):
        self.name = name
        print(f'Звонит {name}')
    def getNumber(self):
        print(self.number)
a = Phone(88005553535,"Xiaomi", 54)
b = Phone(88004354335,"Xiaomi", 59)
c = Phone(88004123312,"Xiaomi", 65)
a.receiveCall("nick")
b.receiveCall("nick")
c.receiveCall("nick")
a.getNumber()
b.getNumber()
c.getNumber()


