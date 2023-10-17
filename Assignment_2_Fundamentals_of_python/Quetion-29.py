#29.Write a Python script to merge two Python dictionaries 

a={'key1':'python','key2':'php','key3':'node.js'}
b={'key1':'Django','key2':'Laravel','key3':'React'}
c=b.copy()
c.update(a)
print(c)
