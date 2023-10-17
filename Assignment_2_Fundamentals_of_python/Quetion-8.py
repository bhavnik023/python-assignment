#8.Write a Python program to convert a list of characters into a string.

a=['T','u','t','o','r','i','a','s','p','o','i','n','t']
b="".join(a)
print("The String is",b)

abc=['P','e','n','c','i','l']
xyz=""
for char in abc:
    xyz += char
print("The String is ",xyz)

abc=['P','e','n','c','i','l']
xyz=""
i=0
while i < len(abc):
    xyz += abc[i]
    i += 1
print("The String is")
