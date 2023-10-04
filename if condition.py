a=int(input("Enter A: "))
b=int(input("Enter b: "))
c=a+b
print("Adition :",c)
c=a-b
print("Subtraction :",c)
c=a*b
print("Multiplication :",c)
c=a/b
print("Division :",c)

 if Condition
 1. Simple if
    if condition:
        statement
 2. if/else
    if condition:
        statement
    else:
        statement
 3. Nested if
    if condition:
        if condition:
            statement
        else:
            statement
    else:
        statement
 4. Ladder if
    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:
        statement
    
a=int(input("Enter A : "))
if a>0:
    print(a," is Positive number")
else:
    print(a," is Negative number")

a=int(input("Enter A :"))
if a%2==0:
    print(a," is Even number")
else:
    print(a," is odd number")

a=int(input("Enter A :"))
b=int(input("Enter B :"))
c=int(input("Enter c :"))
if a>b:
    if a>c:
        print(a," is max number")
    else:
        print(c," is max number")
elif b>c:
    print(b," is max number")
else:
    print(c," is max numer")

a=int(input("Enter A :"))
b=int(input("Enter B :"))
c=int(input("Enter c :"))
if a>b:
    if a>c:
        print(a,"is max num")
    else:
        print(c,"is max num")
elif b>c:
    print(b,"is max num")
else:
    print(c,"is max num")

rno=int(input("Enter Roll No :"))
sname=input("Enter student name :")
s1=int(input("Enter mark of subject 1:"))
s2=int(input("Enter mark of subject 2:"))
s3=int(input("Enter mark of subject 3:"))

total=s1+s2+s3
per=total/3

print("Roll no :",rno)
print("Student name :",sname)
print("total :",total)
print("percentage :",per)

if s1>=40:
    if s2>=40:
        if s3>=40:
            if per>=70:
                print("Distinction")
            elif per>=60:
                print("first class")
            elif per>=50:
                print("second class")
            elif per>=40:
                print("pass class")
            else:
                print("fail")
        else:
            print("you are fail in sub 3")
    else:
        print("you are fail in sub 2")
else:
    print("you are fail in sub 1")
