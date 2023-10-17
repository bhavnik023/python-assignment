
#20.Write a Python function to insert a string in the middle of a string.

s= input("enter your string : ")
def insert_sting_middle(str, word):
	mid = len(str)//2
	return str[:mid]+word+str[:mid]

print(insert_sting_middle(s, 'Python'))

