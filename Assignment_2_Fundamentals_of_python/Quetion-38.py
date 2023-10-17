#38.Write a Python function to check whether a number is in a given range

def myfun(n):
    if n in range(1,30):
        print("this is a range in :",(n))
    else:
        print("outside range")
myfun(5)
