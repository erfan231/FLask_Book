import sqlite3
import request

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS books(book_title TEXT)")
conn.commit()

for x in request.Book_titles:
    cursor.execute("INSERT INTO books(book_title) VALUES (?)", (x,))
    conn.commit()

cursor.execute("SELECT * FROM books")
values = cursor.fetchall()

for y in values:
    print(y)