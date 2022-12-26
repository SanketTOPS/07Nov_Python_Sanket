try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("Sum:",a+b)
except:
    print("Error!")
finally:
    print("This is Finally block.")
