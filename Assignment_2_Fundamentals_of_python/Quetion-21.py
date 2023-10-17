#21.Write a Python program to remove an empty tuple(s) from a list of tuples. 

a=[(),("",),("python","cherry"),(1,2,3,6),()]
a=[b for b in a if b]
print(a)
