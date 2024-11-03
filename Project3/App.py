from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="Lattakone",
            user="postgres",
            password="1234",
            host="localhost",
            port='5432'
        )
        return conn
    except Exception as e:
        print("Error while connecting to database:", e)
        raise

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            year INTEGER NOT NULL,
            genre VARCHAR(100) NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']
    genre = request.form['genre']

    if title and author and year and genre:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, year, genre) VALUES (%s, %s, %s, %s)",
                       (title, author, year, genre))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Book added successfully!', 'success')
    else:
        flash('Please fill in all fields!', 'error')

    return redirect(url_for('index'))

@app.route('/update/<int:book_id>', methods=['POST'])
def update_book(book_id):
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']
    genre = request.form['genre']

    if title and author and year and genre:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET title=%s, author=%s, year=%s, genre=%s WHERE id=%s",
                       (title, author, year, genre, book_id))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Book updated successfully!', 'success')
    else:
        flash('Please fill in all fields!', 'error')

    return redirect(url_for('index'))

@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=%s", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash('Book deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
