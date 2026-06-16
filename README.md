# 📚 Books Scraper Tool

A production-style Python web scraping tool for extracting book data from e-commerce websites.

---

## 🚀 Features

- Pagination handling
- Category filtering (planned/extendable)
- Robust request handling with retries
- Structured architecture (modular design)
- CSV export
- Easy extension to JSON / DB

---

## 🛠 Tech Stack

- Python 3.10+
- requests
- BeautifulSoup4
- argparse
- CSV

---

## 📦 Installation

```bash
git clone https://github.com/funnyvoidd/booksscraper.git
cd booksscraper
pip install -r requirements.txt
```

## ▶️ Usage

```bash
python src/main.py --output data/books.csv
```

## 🧠 Architecture
# This project is modular:

- scraper.py -> crawling logic
- parser.py -> HTML parsing
- exporter.py -> data export
- utils.py -> networking layer
