#5.Write a Python function that takes two lists and returns true if they have
#at least one common member. 

a=[1,3,5,2,3,6,4,7,8,9,4]
b=[10]

out=any(check in a for check in b)

if out:
    print("True")
else:
    print("False")
    
