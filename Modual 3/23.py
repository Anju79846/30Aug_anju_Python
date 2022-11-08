#  Write a Python program to find the repeated items of a tuple.

T= (1,2,3,4,'Anju',2,'Red','Yellow',3)
print(T)
print(T.count("Anju"))

#.............................Looping........
T= (1,2,3,4,'Anju',2,'Red','Yellow',3)
for i in T:
    if T.count(i)>1:
        print(i)
