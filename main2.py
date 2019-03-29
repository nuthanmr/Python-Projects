
from first import add_participants,see_participants

while True:
	choice=input("Enter your choice:\n\
		1.add_participants\n\
		2.see_participants")
	if choice=='1':
		add_participants()
	elif choice=='2':
		see_participants()
	else:
		break

