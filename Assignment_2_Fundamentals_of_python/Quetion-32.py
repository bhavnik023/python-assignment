#32.Write a Python program to print all unique values in a dictionary. 
dict1 = {'A' : [1, 3, 5, 4],
             'B' : [4, 6, 8, 10],
             'C' : [6, 12, 4 ,8],
             'D' : [5, 7, 2]}
print("original dictionary is :",dict1)

x=list(sorted({ele for val in dict1.values() for ele in val}))

print("the unique value list is : ",x)
