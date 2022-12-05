import sqlite3

connection = sqlite3.connect(database='database.db')

with open('schema.sql') as file:
    connection.executescript(file.read())

cur = connection.cursor()

cur.execute("INSERT INTO users_data (username, password) VALUES (?, ?)", ('DimaDrone05', '123qwe123qwe'))
cur.execute("INSERT INTO users_data (username, password) VALUES (?, ?)", ('mary_cat', 'bezibu021'))
cur.execute("INSERT INTO users_data (username, password) VALUES (?, ?)", ('VibeMan', 'longneck11119'))
cur.execute("INSERT INTO users_data (username, password) VALUES (?, ?)", ('old_child', '456asdccd8'))
cur.execute("INSERT INTO users_data (username, password) VALUES (?, ?)", ('david87', '78898kuromin'))
cur.execute("INSERT INTO users_data (username, password) VALUES (?, ?)", ('StanleyColt', 'dog365485a'))
cur.execute("INSERT INTO users_data (username, password) VALUES (?, ?)", ('partyboy69', 'myfavoritenumber69'))

connection.commit()
connection.close()
