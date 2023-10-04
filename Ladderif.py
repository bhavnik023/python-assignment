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
