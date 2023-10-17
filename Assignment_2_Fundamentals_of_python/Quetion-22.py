#22.Write a Python program to unzip a list of tuples into individual lists.

a=[(1,3,5),(2,3,4),(6,8,9)]
print(list(zip(*a)))

b=[(1,3),(3,5),(6,7)]
print(list(zip(*b)))
