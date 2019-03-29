events_dict={'1':'CS','2':'Google It','3':'Treasure Hunt'}
participant_details={}
def add_participants():
	name=input("Enter name:")
	event=input("Enter an event :\n\
		1.cs\n\
		2.google It\n\
		3.treasure hunt\n")
	participant_details[name]=events_dict[event]
	return participant_details

def see_participants():
	for key,value in participant_details.items():
		print(key,value,sep=' - ')

if __name__=='__main__':
	add_participants()
	print(participant_details)
	see_participants()





