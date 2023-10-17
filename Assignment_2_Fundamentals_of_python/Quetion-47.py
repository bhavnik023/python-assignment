#47.Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

from decimal import *
data=list(map(Decimal,'2.0 3.3 1.2 3.2 2.1'.split()))
print("maximum: ",max(data))
print("minimum : ",min(data))

