#  Write a Python program to calculate the area of a trapezoid 
import math   
a=float(input("Enter the upper side of trapizam")) #A=1/2*h(a+b)
b=float(input("Enter the lower side of trapizam")) #A=0.5*h*(a+b)
h=float(input("Enter the hight of trapizam "))

Area=(a+b)*h*0.5
print(Area)