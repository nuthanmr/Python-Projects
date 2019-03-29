
# Write a python program to print the key of a value given as a search element from a dictionary.

# #Input Dictionary
# {'a':"Speckbit", 'b':"World", 'c':"Quiet"}

# Search Element: Speckbit

# #Output
# Key is a.

# #Clue
# Use string formatting while printing.


dict={'a':"Speckbit",'b':"World",'c':"Quiet"}
search=input('Enter the search:')
for key,value in dict.items():
	if search==value:
		print("value is present and the key of the value is:")
		print(key)
	else:
		print("Key not found")
		