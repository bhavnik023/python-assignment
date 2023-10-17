#19.Write a Python program to reverse a tuple.

x=(5,"python","django",4,3,2)
b=list(x)
b.reverse()
c=tuple(b)
print(c)
print(type(c))
