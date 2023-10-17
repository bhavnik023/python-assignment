#11.Write a Python program to count the number of characters (character frequency) in a string

str = "tutorial"
dict={}
for c in str:
    keys=dict.keys()
    if c in keys:
        dict[c] += 1
    else:
        dict[c] =1

print(dict)
