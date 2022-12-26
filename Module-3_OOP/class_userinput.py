class student:
    stid=0
    stnm=''

    def getdata(self):
        self.stid=input("Enter ID:")
        self.stnm=input("Enter Name:")

    def printdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

st=student()
st.getdata()
st.printdata()
