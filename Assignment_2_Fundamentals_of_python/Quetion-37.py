#37.Write a Python function to calculate the factorial of a number (anonnegative integer) 

def myfun(n):
    p=1
    i=1
    while i<=n:
        p=p*i
        i+=1
    return p
myfun(4)
