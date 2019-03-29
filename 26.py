# Write a function for adding the words to a list.

# #Input words
# "Hello"
# "World"
# "Speckbit"
# "Exploratories"

# #Output List
# ["Hello", "World", "Speckbit", "Exploratories"]

list=[]
num=int(input("Enter the number of words:"))
for i in range(1,num+1):
	words=input("Enter the words:")
	list.append(words)
print(list)