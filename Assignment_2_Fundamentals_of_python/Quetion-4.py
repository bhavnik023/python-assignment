#4.Write a Python program to check a list is empty or not.

a=[1,2,3,4,5,6,7,8]
if not a:
    print("List is a empty")
else:
    print("List is not empty \n",a)

a=[]
if len(a)==0:
    print("empty list")
else:
    print("List is not empty\n",a)
