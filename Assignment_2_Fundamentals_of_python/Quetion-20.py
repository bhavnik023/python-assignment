#20.Write a Python program to replace last value of tuples in a list.

a=[(12,332,34),(23,12,43),(32,12,54)]
for i in a:
    print(i[:-1]+(10,))

b=[(1,2,3),(4,5,6),(7,8,9)]
for i in b:
    print(i[:-1]+(100,))
