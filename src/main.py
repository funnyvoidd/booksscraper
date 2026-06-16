import argparse
from scraper import scrape
from exporter import export_csv

BASE_URL = "https://books.toscrape.com/catalogue/page-1.html"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--category", type=str)
    parser.add_argument("--output", type=str, default="data/books.csv")

    args = parser.parse_args()

    data = scrape(BASE_URL)

    export_csv(data, args.output)

    print(f"Done. Saved to {args.output}")


if __name__ == "__main__":
    main()