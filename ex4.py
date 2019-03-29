list1=[1,2,3,2,0,65,21,4,2,10]
list2=[]
search=int(input("enter the search:"))

for i,val in enumerate(list1):
	if val is search:
		list2.append(i)
print(list2)
