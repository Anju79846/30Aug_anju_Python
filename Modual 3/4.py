# Write a Python program to remove duplicates from a list.
"""item = ["Anju","pooja","Bhoomi","pooja","Anju"]

dup_item= set()
uniq_item =[]
for x in item:
    if x not in dup_item:       #looping trough
        uniq_item.append(x)
        dup_item.add(x)

print(dup_item) 
print(uniq_item)       
"""
#...................removing duplicated from the list using set() 
num= [11,10,23,11,26,12,13,13,10,26.25]
num=list(set(num))
print(num)

