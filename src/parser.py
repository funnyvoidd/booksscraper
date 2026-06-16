from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_rating(tag):
    mapping = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    for cls in tag.get("class", []):
        if cls in mapping:
            return mapping[cls]
    return 0


def parse_books(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for b in soup.select("article.product_pod"):
        books.append({
            "title": b.h3.a["title"],
            "price": b.select_one(".price_color").text,
            "rating": get_rating(b.select_one(".star-rating")),
            "availability": b.select_one(".availability").text.strip(),
            "image_url": urljoin(base_url, b.img["src"])
        })

    return books