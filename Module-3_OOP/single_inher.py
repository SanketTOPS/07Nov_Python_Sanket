class father:
    car=0
    bal=0

    def getdata(self):
        self.car=input("Enter Car details:")
        self.bal=input("Enter Bank Balance details:")

class son(father):
    def printdata(self):
        print("Total car:",self.car)
        print("Total Bank Balance:",self.bal)

sn=son()
sn.getdata()
sn.printdata()