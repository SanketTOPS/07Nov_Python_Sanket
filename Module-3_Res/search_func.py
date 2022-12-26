import re

mystr="This is Python!"

x=re.search('is',mystr)
print(x)

if x: #true
    print("Success!")
else:
    print("Error!")
