#Write a Python function that takes two lists and returns true if they have at least one common member.
from operator import truediv

list1=[1,2,3,4,5]
list2=[1,3,5,7,9]
def common_number(list1,list2):
    
    for x in list1:
        for y in list2:
            if x==y:
                print("true")
                 
            else:
                print("false")


print(common_number(list1,list2))

