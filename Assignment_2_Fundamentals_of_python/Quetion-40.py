#40.Write a Python function that checks whether a passed string is palindrome or not 

mystr='aIbohPhoBiA'

mystr=mystr.casefold()

revstr=reversed(mystr)

if list(mystr)==list(revstr):
    print("The String is a palindrome")
else:
    print("the string is not a palindrome")

