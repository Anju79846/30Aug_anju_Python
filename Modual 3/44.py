#  Write a Python function to check whether a number is in a given range
"""def test_range(n):
    if n in range(0,20):
        print("number is in range")
    else:
        print("number is out of range")    
test_range(25)      
"""

#...................................user_input..........
def test_range(n):
    
    if n in range(0,20):
        print("number is in range")
    else:
        print("number is out of range") 
num=int(input("Enter the number"))        
test_range(num)        
