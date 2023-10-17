#6.Write a Python program to generate and print a list of first and last 5
#elements where the values are square of numbers between 1 and 30. 
    
def myfun():
    a=[]
    for i in range(1,30):
        a.append(i**2)
    print(a[:5])
    print(a[-5:])
myfun()

a=[]
for i in range(1,30):
    a.append(i**2)
print(a[:5])
print(a[-5:])
