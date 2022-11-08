# Write a Python program to replace last value of tuples in a list.
T=(1,5,89,2.6,"Red","milk") #Tuple
list=list(T)  # Convert to list
print(list)
list[5]="Yellow"
print(list)
T=tuple(list)  #convert back list to tuple
print(T)