mytup=[]

n=int(input("Enter an elements:")) #n=5

for i in range(n):
    city=input("Enter City name:")
    mytup.append(city)
    

print(tuple(mytup))
