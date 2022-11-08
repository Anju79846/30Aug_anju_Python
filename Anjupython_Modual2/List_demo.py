list1= [1,2,3,4,5]
list2= ["Anju","Pooja","Bhumi"]
list2.extend("Sanju")
list2.append("kajal")
list2.reverse()

print(list2)
list3= list1+list2
print(list3)

if 7 in list1:
    print("7 is available")
else:
    print("7 is not available")
print("Length of list",len(list1))
print("Length of list",len(list2))    

print(['Hi']*4)


#.........list patten......................
for i in range(0,10):
    print("*"*i)

## List operations..................................
"""a =[]
for i in range(10):
    a.insert(3,10)
    print(a)
"""
        