from flask import Flask, render_template
import request
import sqlite3
import requests
import bs4

conn = sqlite3.connect("book_db.db")
cursor = conn.cursor()


def create_table(conn):
    cursor.execute("CREATE TABLE IF NOT EXISTS books(book_name TEXT price_of_book TEXT)")
    conn.commit()


def inserting_data(conn):

    for n in range(1, 51):  # pages(1 to 50)
        website_url = "http://books.toscrape.com/catalogue/page-{}.html"
        website_request = requests.get(website_url.format(n))

        soup = bs4.BeautifulSoup(website_request.text, "lxml")
        books = soup.select(".product_pod")  # get all the books

    for book in books:  # check for 2 star rating books
        if len(book.select(".star-rating.Five")) != 0:  # if the list is not empty, if list is empty means the book doesn't have 2 star
            book_title = book.select("a")[1]["title"]  # check the <a> tag to find the title
            book_price = book.select(".price_color")

            for price in book_price:
                pass
            # in this case the book has 2 <a> tag one for the image/link and the scond one([1]) contains the 'title' tag in it
            # so we search the <a> tag and grab the title from it

    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()

    if len(result) <= 0:
        cursor.execute('INSERT INTO books(book_name) VALUES (?)', (price))
        conn.commit()
    else:
        pass


def fetch_data(conn):
    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()

    for x in result:
        print(x)

create_table(conn)
inserting_data(conn)
fetch_data(conn)

"""
app=Flask(__name__)


hmm="hi"

request.main()
num=-1


def a(number):
    global num
    num += 1
    return request.Book_titles[number]




app.jinja_env.globals.update(hmm)


@ app.route("/")
def main():
    while num < len(request.Book_titles):
        return a(num)


@ app.route("/main")
def books():
    data=request.Book_titles
    price=request.Book_prices
    return render_template('table.html', data=data, price=price)


app.run(debug=True)
"""