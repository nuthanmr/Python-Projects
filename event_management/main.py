from models import *    # * is used to imports everything

def add_events():
	event_name=input("Enter the name of the event you want to add:")

	EventsList.create(event_name=event_name)

def see_events():
	events=EventsList.select()

	for event in events:
		print(event.id, event.event_name, sep="-")

def add_participants():
	participant_name=input("Enter the name of the participant:")
	events=EventsList.select()
	for event in events:
		print(event.id, event.event_name, sep="-")
	event_id=int(input("Select the event in which the participant wants to participate in:\n"))

	ParticipantList.create(participant_name=participant_name,event_name=event_id)

def see_participants():
	for participant in ParticipantList.select():
		print(EventsList.get(participant.event_name_id))
		print(participant.id, participant.participant_name, EventsList.get(participant.event_name_id).event_name, sep=" - ")
while True:
	choice=input("Enter the action that you want to do:\n 1.Add Event\n 2.See Event \n 3.add_participants\n 4.see_participants\n 5.exit\n")

	if choice=='1':
		add_events()

	elif choice=='2':
		see_events()

	elif choice=='3':
		add_participants()

	elif choice=='4':
		see_participants()

	else:
		break


