#10.Write a Python program to find the second smallest number in a list. 
a=[]
n=int(input("Enter no : "))
for i in range(1,n+1):
    x=int(int(input("Enter no : ")))
    a.append(x)
a.sort()
print("The Sorted List: ",a)
print("The second smallest number in a list",a[1])
