#  Write a Python program to find the highest 3 values in a dictionary
from operator import index


fruits= {"Apple":40,"Banana":63,"Cherry":89,"Mango":23,"Papaya":45}
Costly_fruits= sorted(fruits,key=fruits.get,reverse=True)
print(Costly_fruits)
for i in range(3):
    print(Costly_fruits[i])