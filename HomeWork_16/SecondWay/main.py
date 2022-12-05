from flask import Flask, render_template
import sqlite3


def get_db_connection():
    connection = sqlite3.connect('db_init/database.db')
    connection.row_factory = sqlite3.Row
    return connection


app = Flask(__name__)


@app.route('/')
def index():
    connection = get_db_connection()
    users_data = connection.execute('SELECT * FROM users_data').fetchall()
    return render_template('index.html', users_data=users_data)


if __name__ == '__main__':
    app.run(debug=True)


