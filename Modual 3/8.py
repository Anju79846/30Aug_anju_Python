# Write a Python function that takes a list and returns a new list with unique elements of the first list.


list=("python","JAVA","C","python","C","Ruby","JAVA")
unique_list =[]
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print("given list",list)
print("unique list",unique_list)        
