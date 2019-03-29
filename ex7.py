my_dict={1:"speckbit",2:"world",3:"quiet"}
search=input("enter the word")
for i in my_dict:
	if i is search:
		print(True)
	else:
		print(False)