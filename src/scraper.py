from utils import safe_request
from parser import parse_books

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

        url = (
            url.rsplit("/", 1)[0] + "/" + next_btn["href"]
            if next_btn else None
        )

    return all_books