import requests
import bs4

Book_titles = set()
Book_prices = set()


def main():
    for n in range(1, 51):  # pages(1 to 50)
        website_url = "http://books.toscrape.com/catalogue/page-{}.html"
        website_request = requests.get(website_url.format(n))

        soup = bs4.BeautifulSoup(website_request.text, "lxml")
        books = soup.select(".product_pod")  # get all the books

        for book in books:  # check for 2 star rating books
            if len(book.select(".star-rating.Five")) != 0:  # if the list is not empty, if list is empty means the book doesn't have 2 star
                book_title = book.select("a")[1]["title"]  # check the <a> tag to find the title
                book_price = book.select(".price_color")

                for x in book_price:
                    Book_prices.add(x.text)
            # in this case the book has 2 <a> tag one for the image/link and the scond one([1]) contains the 'title' tag in it
            # so we search the <a> tag and grab the title from it
                Book_titles.add(book_title)

"""
if __name__ == "__main__":
    main()
    print(Book_titles)
    print(len(Book_titles))

    def a(number):
        global num
        num += 1
        return Book_titles[number]


else:
    pass:
    main()
    """

main()