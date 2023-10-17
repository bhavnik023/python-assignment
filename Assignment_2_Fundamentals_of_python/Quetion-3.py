#3.Write a Python program to remove duplicates from a list. 

a=[1,2,5,7,9,8,7,6,12,3,23,12,43]
com=[]
ncom=[]
for i in a:
    if (a.count(i)>1):
        com.append(i)
    else:
        ncom.append(i)
print("Duplicate value",(list(set(com))))
print("original value",ncom)
