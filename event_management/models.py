import peewee

db=peewee.SqliteDatabase("events.db")

class EventsList(peewee.Model):
	event_name=peewee.TextField()

	class Meta:      #to specify the database to which the tables belong
		database=db

class ParticipantList(peewee.Model):
	participant_name=peewee.TextField()
	event_name=peewee.ForeignKeyField(EventsList)

	class Meta:
		database=db

db.connect()
db.create_tables([EventsList,ParticipantList])


