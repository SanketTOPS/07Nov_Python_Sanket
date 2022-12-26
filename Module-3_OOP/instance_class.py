class student:
    stid=101
    stnm='Sanket'

    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)
    
# Calling via Object
"""st=student()
st.getdata()
st.stid=102
st.stnm='Nirav'
st.getdata()"""

# ------------------------------------------ #
# Calling via Instance
student().getdata()
student().stid=102
student().stnm='Nirav'
student().getdata()