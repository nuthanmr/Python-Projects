details={}
for i in range(3):
	key=input("enter USN:")
	value=input("enter Name:")
	if key not in details.keys():
		details[key]=value
print(details)