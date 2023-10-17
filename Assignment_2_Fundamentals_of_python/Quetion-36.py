#36.Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string: 'w3resource' 

st = input("Enter a string: ")
dic = {} 
for ch in st:
    if ch in dic:
        dic[ch] += 1
    else:
        dic[ch] = 1
for key in dic:
    print(key,':',dic[key])
