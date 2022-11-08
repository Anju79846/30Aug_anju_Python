#  Write a Python program to combine values in python list of dictionaries. 
from collections import Counter

item_list=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, {'item': 'item1', 'amount': 750}] 

result= Counter()
for i in item_list:
    result[i['item']]+=i['amount']
print(result)    