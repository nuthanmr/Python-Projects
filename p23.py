# Write a Python program to insert a given string at the beginning of each item in the list.  


# Sample list : 
# [1,2,3,4]


# string : emp
	
# Expected output :  
# ['emp1', 'emp2', 'emp3', 'emp4']

num=[1,2,3,4]

print(['emp{0}'.format(i) for i in num])