#17.Write a Python function that takes a list of words and returns the length of the longest one.

s = ["tpython", "Jane", "quick", "gandinagar", 'rajkot', 'gujrat']
print("The list is :",s)


def longest_length_string(s):
   s_len=len(s[0])
   tamp = s[0]
   for i in s:
        if len(i)>s_len:
            s_len=len(i)
            tamp=i
   print("Longest word in string is : ",tamp)
   print("longest word",tamp,"len is :",s_len)

longest_length_string(s)
