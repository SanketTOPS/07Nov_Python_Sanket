class grandfather:
    house=0
    gold=0

    def g_getdata(self):
        self.house=input("Enter House details:")
        self.gold=input("Enter Gold details:")

class father(grandfather):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("Enter Car details:")
        self.bal=input("Enter Bank balance details:")

class son(father):
    def printdata(self):
        print("------Grandfather's Data------")
        print("House:",self.house)
        print("Gold:",self.gold)
        print("------Father's Data------")
        print("Car:",self.car)
        print("Bank Balance:",self.bal)

sn=son()
sn.g_getdata()
sn.f_getdata()
sn.printdata()