class ashok:
    aid=0
    asub=''

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class nirav:
    nid=0
    nsub=''

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")

class hitesh:
    hid=0
    hsub=''

    def h_getdata(self):
        self.hid=input("Enter Hitesh's ID:")
        self.hsub=input("Enter Hitesh's Subject:")

class tops(ashok,nirav,hitesh):
    def printdata(self):
        print("-------Ashok's Data-------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("-------Nirav's Data-------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("-------Hitesh's Data-------")
        print("Hitesh's ID:",self.hid)
        print("Hitesh's Subject:",self.hsub)


tp=tops()
tp.a_getdata()
tp.n_getdata()
tp.h_getdata()
tp.printdata()