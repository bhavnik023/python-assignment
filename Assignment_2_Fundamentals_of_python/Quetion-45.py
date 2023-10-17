#45.Write a Python program to calculate surface volume and area of a cylinder
import math

r=float(input("Enter r of a cylinde"))

h=float(input("Enter the Height of a cylinde"))

s_area=2*math.pi*pow(r,2)*h

volume=math.pi*pow(r,2)*h

print("surface area of a cylinder wll be %.2f" %s_area)
print("volume of a cylinder will be  %.2f" %volume)
