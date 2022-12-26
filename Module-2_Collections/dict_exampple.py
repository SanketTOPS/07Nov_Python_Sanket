stdata={'id':1,'name':'sanket','age':30}
#print(stdata)
"""print(stdata['age'])
print(stdata.get('name'))
print(len(stdata))"""

"""stdata['id']=2
stdata['name']='mitesh'
print(stdata)"""

# ------------------------------------- #

"""if 'name' in stdata:
    print("Yes....")
else:
    print("Nooo")"""

"""print(stdata.keys())
print(stdata.values())

if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Nooo")
"""
# --------------------------------------------- #

print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

stdata['sub']='Python'
stdata.pop('id')
#del stdata['name']
#stdata.clear()
#del stdata
print(stdata)