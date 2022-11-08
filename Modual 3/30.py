#  Write a Python script to check if a given key already exists in a dictionary. 
stdata={"Anju":4 ,"Pooja":10 ,"Bhumi":8 ,"Mukul":24}
user_input=input("Enter the key you want to check")
if user_input in stdata:
    print("key is alredy exixts")
    print("value is",stdata[user_input])
else:
    print("this is new key")
       
