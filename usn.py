data={}
for i in range(4):
	usn=input("Enter the usn:")
	name=input("Enter the name:")
	if usn not in data.keys():
		data[usn]=name
print(data)
