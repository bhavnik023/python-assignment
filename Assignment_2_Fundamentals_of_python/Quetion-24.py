#24.Write a Python script to sort (ascending and descending) a dictionary by value.

a={'num6':6,'num3':3,'num2':2,'num1':1,'num4':4,'num5':5}
l=list(a.items())
l.sort()
print("Ascending order is ",l)
l.sort(reverse=True)
print("Descending order is",l)

d=dict(l)
print("Dictionary",d)
