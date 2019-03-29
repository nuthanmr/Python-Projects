usn=[1,2,3]
names=['ramesh','suresh','andy']
database=[]
for i in range(len(usn)):
	database.append((usn[i],names[i]))
print(dict(database))
