# Write a Python function to reverses a string if its length is a multiple of 4.
Name=input("name String:")

if(len(Name)%4==0):
   print(Name[::-1])
else:
   print("not valid")