#   Write a Python program to read a random line from a file. 

import random
# f=open("file1.txt",'a') # open fil
# print(f)

fl =open("file1.txt",'r')
# print(fl)
line=fl.readlines()
# print(line)
length=len(line)
fl1=random.choices(line)
print(fl1)
fl.close()
