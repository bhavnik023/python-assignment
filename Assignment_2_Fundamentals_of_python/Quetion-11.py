#11.Write a Python program to get unique values from a list 
lst=["10","20","40","50","60","10","40"]
print("Orignal list",lst)
myset=set(lst)
mynewlst=list(myset)
print("list in a unique number : ",mynewlst)
