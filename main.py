from flask import Flask, render_template
import sqlite3
import request

class Books:
    def __init__(self):
        conn = sqlite3.connect("book.db")
        cursor = conn.cursor()
        self.conn = conn
        self.cursor = cursor
        self.Book_titles = request.Book_titles
        self.Book_price = request.Book_prices
    
    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books_new(book_id INTEGER PRIMARY KEY, book_name TEXT, book_price TEXT)")
        self.conn.commit()

    def insert_data(self):
        self.cursor.execute("SELECT * FROM books")
        value = self.cursor.fetchall()
        num = 0
        if len(value) == 0 or len(value) < 1:
            for price in self.Book_price:
                self.cursor.execute("INSERT INTO books_new(book_price) VALUES (?)", (str(price),))
        for book in self.Book_titles:
            self.cursor.execute("INSERT INTO books_new(book_name) VALUES (?)", (book,))
            self.conn.commit()
        else:
            print("Data already exists")

    def show_values(self):
        self.cursor.execute("SELECT * FROM books")
        value = self.cursor.fetchall()
        #if you want to see the values one by one
        
        for book in value:
            print(book)
        

    def query_database(self,book_to_look_for):
        self.cursor.execute("SELECT * FROM books WHERE book_name == {book_to_look_for}")
        data = self.cursor.fetchall()
        for x in data:
            print(x)
        self.conn.commit()

    def picky_query(self,search_for):
        self.cursor.execute("SELECT book_name FROM books WHERE book_id == {search_for}")
        data = self.cursor.fetchall()
        self.conn.commit()

        #self.cursor.execute("SELECT book_price FROM books WHERE book_name == {search_for}")
        #data = self.cursor.fetchall()


    def delete_data(self,value_to_delete):
        self.cursor.execute("DELETE FROM books WHERE book_name == {value_to_delete}")
        self.conn.commit()

    def delete_all_data(self):
        self.cursor.execute("DELETE FROM books")
        self.conn.commit()
 


start = Books()
start.delete_all_data()
start.create_table()
start.insert_data()
start.show_values()


app=Flask(__name__)

@app.route("/")
def books():
    data=start.Book_titles
    price= start.Book_price
    return render_template('table.html', data=data, price=price)


app.run(debug=True)