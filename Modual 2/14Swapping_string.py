# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.
str1= "anju"
str2= "kakran"
str1,str2=str2,str1
fs= str1[0]
ls= str2[-2]
print(fs,ls,end="")