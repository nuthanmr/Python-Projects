# Write a python program to print all the key value pairs in a given dictionary in the given format.

# Input Dictionary
# {1:"Speckbit", 2:"World", 3:"Quiet"}

# #Output
# 1--Speckbit
# 2--World
# 3--Quiet

# #Clue
# Use string formatting while printing.

dict1={1:"Speckbit", 2:"World", 3:"Quiet"}

for key,value in dict1.items():
	print(f"{key} -- {value}")