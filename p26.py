#  write a function for adding the words to a list.

# #Input words
# "Hello"
# "World"
# "Speckbit"
# "Exploratories"

# #Output List
# ["Hello", "World", "Speckbit", "Exploratories"]

# #clue
# mylist = []

# word = input()

# def add_to_list(word):
#     # your logic

mylist=[]
num=int(input("enter the numbers of words:"))
def add_to_list():
	for i in range(1,num+1):
		word=input("Enter the words:")
		mylist.append(word)
	return mylist

if __name__=='__main__':
	add_to_list()
	print(mylist)




