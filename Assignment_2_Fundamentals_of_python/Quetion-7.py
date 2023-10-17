#7.Write a Python function that takes a list and returns a new list with unique
#elements of the first list.

def unique_list(l):
    x=[]
    for a in l:
        for a not in x:
            x.append(a)
        return x

print(unique_list(1,2,3,4,1,3,4,5,6,7,9,7,8))
