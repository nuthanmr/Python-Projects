import sqlite3

con=sqlite3.connect("books_db.sqlite3")
cur=con.cursor() #pointer to a instruction

try:
	cur.execute("CREATE TABLE books (id INTEGER PRIMARY KEY,name TEXT,rating REAL )")
except sqlite3.OperationalError:
	print("Table Already exists...")
	
cur.execute("""INSERT INTO books VALUES (1,"PYTHON",4.1)""")
cur.execute("""INSERT INTO books VALUES (2,"C PROGRAM",4.2)""")
cur.execute("""INSERT INTO books VALUES (3,"RUBY",4.5)""")

con.commit()
