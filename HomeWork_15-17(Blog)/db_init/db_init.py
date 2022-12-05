import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as file:
    connection.executescript(file.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content, author) VALUES (?, ?, ?)", ('First post', 'Hello world!', 'Author1'))
cur.execute("INSERT INTO posts (title, content, author) VALUES (?, ?, ?)", ('Second post', 'How are you?', 'Author2'))
cur.execute("INSERT INTO posts (title, content, author) VALUES (?, ?, ?)", ('Third post', 'Goodbye!', 'Author3'))

connection.commit()
connection.close()