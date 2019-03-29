class AccountManager():

	def __init__(self,account_name,account_no,balance,pin):
		self.account_name= account_name
		self.account_no=account_no
		self.balance=float(balance)
		self.pin=pin
		self.transactions=[]
		

	def deposit(self,amount=0.0):
		if amount>10000:
			print("You can't add amount greater than 10000.Please try again")
		elif amount<0:
			print("Invalid deposit amount.Try again")
		else:
			self.balance+=amount
			transaction=('+'+str(amount),self.balance)
			self.transactions.append(transaction)


	def withdraw(self,amount=0.0):
		if (self.balance-amount)<0:
			print("Insufficient balnace")
		elif self.balance<=3000:
			print("Low balance.Deposit money")
		else:
			self.balance-=amount
			transaction=('+'+str(amount),self.balance)
			self.transactions.append(transaction)


	def show_balance(self):
		print(f"The balance is {self.balance}")

	def account_statement(self):
		return self.transactions

# -----------------------------------------------------------------------------------------------------

# Child Class 1

class SavingsAccount(AccountManager):

	def __init__(self,account_name,account_no,balance,pin):
		self.account_name=account_name
		self.account_no=account_no
		self.pin=pin
		self.transactions=[]

		if balance<3000:
			print("Minimum opening balance should be 3000")
		else:
			self.balance=balance

# Child Class 2

class CurrentAccount(AccountManager):
	def __init__(self,account_name,account_no,balance,pin):
		self.account_name=account_name
		self.account_no=account_no
		self.pin=pin
		self.transactions=[]

		if balance<10000:
			print("Minimum opening balance should be 10000")
		else:
			self.balance=balance

	def withdraw(self,amount=0.0):
		if (self.balance-amount)<0:
			print("Insufficient Balance")

		else:
			self.balance-=amount
			transaction=('-'+str(amount),self.balance)
			self.transactions.append(transaction)