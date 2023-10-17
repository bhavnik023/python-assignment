#6.Write a Python program to test whether a passed letter is a vowel or not.

a=input("Enter character : ")

if a.lower() in ('a','v','c','s','d'):
    print(vowel)
elif a.upper() in ('A','V','C','S','D'):
    print(vowel)
else:
    print("consonat")
