from bs4 import BeautifulSoup
from urllib.parse import urljoin
from utils import safe_request
from src.parsers.books import parse_books

def scrape(start_url):
    url = start_url
    all_books = []

    while url:
        r = safe_request(url)
        if not r:
            break

        books = parse_books(r.text, url)
        all_books.extend(books)

        next_btn = BeautifulSoup(r.text, "html.parser").select_one("li.next a")

        url = urljoin(url, next_btn["href"]) if next_btn else None

    return all_books