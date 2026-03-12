import requests
from bs4 import BeautifulSoup
from app.database.db import insert_competitor_price


URL = "http://books.toscrape.com/"


def scrape_books():

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text
        price = price.replace("£", "").replace("Â", "").strip()
        price = float(price)

        insert_competitor_price(
            product_name=title,
            price=price,
            source="books.toscrape"
        )

        print(f"Saved: {title} - {price}")


if __name__ == "__main__":
    scrape_books()