class student:
    stid=12
    stnm='Sanket'

    def getdata(self):
        print("This is Student Class.")
    
    def getsum(self,a,b):
        print("Sum:",a+b)


# Object of class
st=student()
print(st.stid)
print(st.stnm)
st.getdata()
st.getsum(23,43)
