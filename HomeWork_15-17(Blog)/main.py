from flask import Flask, render_template, request, redirect, url_for
import sqlite3


def get_db_connection():
    connection = sqlite3.connect('db_init/database.db')
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


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']

        connection = get_db_connection()
        connection.execute('INSERT INTO posts (title, content, author) VALUES (?, ?, ?)', (title, content, author))
        connection.commit()
        connection.close()

        return redirect(url_for('index'))
    else:
        return render_template('create.html')


@app.route('/<int:post_id>/edit', methods=['GET', 'POST'])
def edit(post_id):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']

        connection = get_db_connection()
        connection.execute('UPDATE posts SET title = ?, content = ?, author = ? WHERE id = ?',
                           (title, content, author, post_id)
                           )
        connection.commit()
        connection.close()

        return redirect(url_for('index'))
    else:
        post = get_post(post_id)
        return render_template('create.html', post=post)


@app.route('/<int:post_id>/delete', methods=['POST'])
def delete(post_id):
    connection = get_db_connection()
    connection.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    connection.commit()
    connection.close()
    return redirect(url_for('index'))


@app.route('/<author>')
def author(author):
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts WHERE author = ?', (author,)).fetchall()
    connection.commit()
    connection.close()
    return render_template('author.html', posts=posts, author=author)


@app.route('/delete_all_posts')
def delete_all_posts():
    connection = get_db_connection()
    connection.execute('DELETE FROM posts')
    connection.commit()
    connection.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

