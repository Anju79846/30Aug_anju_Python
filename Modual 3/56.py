#  Write a Python program to calculate surface volume and area of a cylinder 
import math
r=float(input("Enter the radius of cylinder"))
h=float(input("Enter the height of cylinder"))

Surface_value=(math.pi*r*r*h)
print("Surface value of cylinder",Surface_value)

Area=(2*math.pi*r*h)
print("Area of cylinder",Area)