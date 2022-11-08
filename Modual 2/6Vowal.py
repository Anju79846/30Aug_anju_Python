"""x= input("Enter sentsnce")
for i in x:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        print("this latter is Vowal",i)
"""

x= input("Enter sentsnce")
count=0
for i in x:

    if i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u":

        print(i)
        count=count=1
    if count==0:
        print("no Vowal found")    
    else:
        print("number of vowals:",count)    
