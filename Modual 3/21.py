#  Write a Python program to reverse a tuple.
Tuple_1 =(1,2,3,4,5,6)

list=list(Tuple_1) # Tuple convert to list
list.reverse() # Reverse list

Tuple_1=tuple(list)

print(Tuple_1)
#..........................................
t =(1,2,3,4,5,6)
print(tuple(reversed(t))) #Reverse tuple

print(t[ : :-1])# slicing




