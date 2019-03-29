from tree import Tree

employee_password={}
password=100

print("Welcome To Tree Census Committee")

while True:
	print("Hey!What Would You Like To Do?\n\n\
		1.Add Employees\n\
		2.Create Password\n\
		3.Reset Password\n\
		4.Exit\n")
	choice=int(input("Enter Your Choice:"))

	if choice==1:
		employee_name=input("Enter the name of the employee:")
		employee_gender=input("Enter the gender of the employee:")
		employee_password[password]=Tree

