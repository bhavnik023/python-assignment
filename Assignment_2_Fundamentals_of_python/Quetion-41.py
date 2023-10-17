#41.Write a Python program to read a random line from a file. 

a=open("Demo1.txt","w")
a.write("This is file management demo using python. welcome to python")
a.close()

import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('Demo1.txt'))
