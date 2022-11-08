#Write a Python program to count the number of strings where the string length is 2 or more and
#  the first and last character are same from a given list of strings.

words =["aba","121","kgf","dfd"]
count =0
for word in words:
    if len(words)>1 and word[0]==word[-1]:
        count +=1
    print("Given string is",words)    
print("No of count is",count)    