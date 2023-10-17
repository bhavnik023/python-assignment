#2.Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character are same from a given list of strings. 

s=0
lst=["222","abc","12","34","67","232""apple","cherry"]
for i in lst:
    if len(i)>1 and i[0]==i[-1]:
        print(i)
        s=s+1
print(s)
