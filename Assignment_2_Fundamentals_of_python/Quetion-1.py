#1.Write a Python function to get the largest number, smallest num and sum of all from a list.

lst=[]
n=int(input("Enter NO : "))
def myfun(lst):
    for i in range(n):
        number=int(input("Enter no : "))
        lst.append(number)
    print("Mamximum element in the list is : ",max(lst),"Minimum element in the list is : ",
          min(lst))
myfun(lst)
        
a=[34,56,76,23,21,12]
print("Largest no : ",max(a))
print("Samllest no : ",min(a))

a=[1,3,5,46,42,7,8,97,34,45,67]
a.sort()
print(a[-1])

lst=[]
num=int(input("Enter no : "))

for i in range(1,num+1):
    ls=int(input("Enter no : "))
    lst.append(ls)
print("Largest no : ",max(lst))
print("Samllest no : ",min(lst))
