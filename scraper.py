import csv
import argparse
import logging
import requests

from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.parse import urljoin

logging.basicConfig(
    filename="scraper.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

BASE_URL = "https://books.toscrape.com/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    )
}

REQUEST_TIMEOUT = 10

def safe_request(url):
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        response.encoding = "utf-8"  # <-- ВАЖНО

        return response

    except requests.RequestException as e:
        logger.error(f"Ошибка запроса {url}: {e}")
        return None

def get_categories():
    response = safe_request(BASE_URL)

    if not response:
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")

    categories = {}

    for category in soup.select(".side_categories ul li ul li a"):
        name = category.get_text(strip=True)
        href = category["href"]

        categories[name.lower()] = urljoin(BASE_URL, href)

    return categories


def get_rating(star_tag):
    classes = star_tag.get("class", [])

    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    for cls in classes:
        if cls in ratings:
            return ratings[cls]

    return 0


def parse_page(url):
    response = safe_request(url)

    if not response:
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    for article in soup.select("article.product_pod"):
        title = article.h3.a["title"]

        price = article.select_one(".price_color").text.strip()

        availability = (
            article.select_one(".availability")
            .get_text(strip=True)
        )

        rating = get_rating(article.select_one(".star-rating"))

        image = article.select_one("img")["src"]
        image_url = urljoin(url, image)

        books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
            "image_url": image_url
        })

    next_button = soup.select_one("li.next a")

    next_page = None

    if next_button:
        next_page = urljoin(url, next_button["href"])

    return books, next_page


def scrape(category=None):
    if category:
        categories = get_categories()

        category_url = categories.get(category.lower())

        if not category_url:
            print(f"Категория '{category}' не найдена.")
            return

        start_url = category_url
    else:
        start_url = BASE_URL

    all_books = []

    current_url = start_url

    with tqdm(desc="Сбор книг") as pbar:

        while current_url:
            books, current_url = parse_page(current_url)

            all_books.extend(books)

            pbar.update(len(books))

    save_to_csv(all_books)

    print(f"\nГотово. Собрано книг: {len(all_books)}")


def save_to_csv(data):
    with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "title",
                "price",
                "rating",
                "availability",
                "image_url"
            ]
        )

        writer.writeheader()
        writer.writerows(data)


def main():
    parser = argparse.ArgumentParser(
        description="Books To Scrape parser"
    )

    parser.add_argument(
        "--category",
        type=str,
        help="Название категории"
    )

    args = parser.parse_args()

    scrape(args.category)


if __name__ == "__main__":
    main()