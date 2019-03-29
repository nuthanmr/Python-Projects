from bank import AccountManager

accounts={}
account_no=1001
print("-"*50)
print("welcome to Iron Bank")

while True:
	print("Hey! what would you like to do today?\n\n\
		1.Create Savings Account\n\
		2.Create Current Account\n\
		3.Check Transactions\n\
		4.Deposit Amount\n\
		5.Withdraw Amount\n\
		6.Show Balnce\n\
		7.Exit\n") 

	choice=int(input("Enter your option:"))

	if choice==1:
		acc_name=input("Enter account name:")
		balance=input("Enter opening balance amount:")
		pin=int(input("Enter a PIN for your Account:"))

		accounts[account_no]=AccountManager(acc_name,account_no,balance,pin)
		print(accounts)
		print(f"Savings Account created successfully! Your account number is {account_no}")
		account_no+=1


	elif choice==2:
		acc_name=input("Enter account name:")
		balance=input("Enter opening balance amount:")
		pin=int(input("Enter a PIN for your Account:"))

		accounts[account_no]=AccountManager(acc_name,account_no,balance,pin)
		print(accounts)
		print(f"Current Account created successfully! Your account number is {account_no}")
		account_no+=1



	elif choice==3:
		acc_no=eval(input("Enter Account Number:"))
		upin=eval(input("Enter the PIN for your Account:"))

		if upin ==accounts[acc_no].pin:
			statement=accounts[acc_no].account_statement()
			print(statement)

		else:
			print("\n\nInvalid Credentials.Please enter again!\n\n")

	elif choice == 4:
		acc_no = eval(input("Enter Account Number: "))
		upin = eval(input("Enter the PIN for your Account: "))

		if upin == accounts[acc_no].pin:
			amount = int(input("Enter the amount to be deposited: "))
			accounts[acc_no].deposit(amount)

		else:
			print("\n\nInvalid Credentials. Please enter again!\n\n")

	elif choice == 5:
		acc_no = eval(input("Enter Account Number: "))
		upin = eval(input("Enter the PIN for your Account: "))

		if upin == accounts[acc_no].pin:
			amount = int(input("Enter the amount to be withdraw: "))
			accounts[acc_no].withdraw(amount)

		else:
			print("\n\nInvalid Credentials. Please enter again!\n\n")

	elif choice == 6:
		acc_no = eval(input("Enter Account Number: "))
		upin = eval(input("Enter the PIN for your Account: "))

		if upin == accounts[acc_no].pin:
			accounts[acc_no].show_balance()
	else:
		break