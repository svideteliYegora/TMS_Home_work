import sqlite3

connection = sqlite3.connect('../database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('First post!!!', 'Hello everyone!'))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('Second post!!!', 'Goodbye!'))

connection.commit()
connection.close()