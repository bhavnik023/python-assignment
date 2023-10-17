#4.Write python program that swap two number with temp variable and without temp variable.
a=int(input("Enter A no : "))
b=int(input("Enter B no : "))

a,b=b,a

print("A is :",a)
print("B is :",b)

a=int(input("Enter A no : "))
b=int(input("Enter B no : "))

temp=a
a=b
b=temp
print("A is :",a)
print("B is :",b)
