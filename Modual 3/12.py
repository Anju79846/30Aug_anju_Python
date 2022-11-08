#  Write a Python program to get unique values from a list

list=("python","JAVA","C","python","C","Ruby","JAVA")
unique_list =[]
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print("given list",list)
print("unique list",unique_list) 