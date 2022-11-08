#Write a Python script to concatenate following dictionaries to create a new one
n1=int(input("Enter the key-value pairs dictionary"))
d1={}
for i in range(n1):
    k=input("Enter the key")
    v=input("Enter the value")
    d1.update({k:v})
print("Dictionary 1",d1)    

n2=int(input("Enter the key-value pairs dictionary"))
d2={}
for i in range(n1):
    k=input("Enter the key")
    v=input("Enter the value")
    d2.update({k:v})
print("Dictionary 1",d2)  

d1.update(d2)
print("concenate Dictionary",d1)
