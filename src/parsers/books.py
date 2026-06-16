from bs4 import BeautifulSoup


def parse(html, base_url):
    soup = BeautifulSoup(html, "html.parser")

    items = []

    for b in soup.select("article.product_pod"):
        items.append({
            "title": b.h3.a["title"],
            "price": b.select_one(".price_color").text,
            "rating": len(b.select_one(".star-rating")["class"]) - 1,
            "availability": b.select_one(".availability").text.strip()
        })

    next_btn = soup.select_one("li.next a")
    next_url = next_btn["href"] if next_btn else None

    return items, next_url