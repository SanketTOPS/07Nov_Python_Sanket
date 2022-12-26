import re

#sanket2020@gmail.com
email=input("Enter an email:")

email_ptrn="^[a-z0-9._]+[@]+[a-z]+[\.]+[a-z]{2,}$"

x=re.findall(email_ptrn,email)

if x:
    print("Valid Email")
else:
    print("Error! Inavlid Email")