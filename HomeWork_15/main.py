from flask import Flask, render_template, request, redirect, url_for
import sqlite3


def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    connection.close()
    return post


app = Flask(__name__)


@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        connection = get_db_connection()
        connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
        connection.commit()
        connection.close()

        return redirect(url_for('index'))
    else:
        return render_template('create.html')


@app.route('/<int:post_id>/edit/', methods=['GET', 'POST'])
def edit(post_id):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        connection = get_db_connection()
        connection.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, post_id))
        connection.commit()
        connection.close()
        return redirect(url_for('index'))
    else:
        post = get_post(post_id)
        return render_template('edit.html', post=post)


@app.route('/<int:post_id>/delete/', methods=['POST'])
def delete(post_id):
    connection = get_db_connection()
    connection.execute('DELETE FROM posts Where id = ?', (post_id,))
    connection.commit()
    connection.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

