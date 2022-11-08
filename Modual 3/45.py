#  Write a Python function to check whether a number is perfect or not
def perfact(n):
    sum=0
    for i in range(1,n):
        if n %i ==0:
             sum = sum+i
       
        
num=int(input("Enter a number"))    
a=perfact(num)
if num == sum:
    print("num is perfact")
else:
    print("num is not perfact")    
