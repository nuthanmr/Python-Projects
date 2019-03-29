import sqlite3
con=sqlite3.connect("movies_db.sqlite3")
cur=con.cursor()
try:
	cur.execute("CREATE TABLE movies (id INTEGER PRIMARY KEY, name TEXT, release_year INTEGER)")
except sqlite3.OperationalError:
	print("Table Already exists...")

cur.execute("""INSERT INTO movies VALUES (1, "Avatar", 2009)""")
cur.execute("""INSERT INTO movies VALUES (2, "Titanic", 1997)""")
cur.execute("""INSERT INTO movies VALUES (3, "Titanic1", 1997)""")
cur.execute("""INSERT INTO movies VALUES (4, "Shrek 2", 2004)""")
cur.execute("""INSERT INTO movies VALUES (5, "The Lion King", 1994)""")
cur.execute("""INSERT INTO movies VALUES (6, "Disney's Up", 2009)""")

con.commit()