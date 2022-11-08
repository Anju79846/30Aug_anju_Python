# Write a Python program to get the Factorial number of given number
num = int(input("Enter a number:"))
fact=1
if num<0:
    print("factorial does not exixt of nagative number:")
elif num==0:
    print("factorail of 0 is 1:")
else:
        for i in range(1, num +1):
            fact=fact*i
            print("factorail of" ,num, "is" ,fact,)