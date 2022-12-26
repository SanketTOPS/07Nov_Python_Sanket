class student:
    __stid=12
    __stnm='Nirav'

    def __getdata(self):
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    
    def newfunc(self):
        self.__getdata()


st=student()
#print(st.stid)
#print(st.stnm)
#st.getdata()
st.newfunc()