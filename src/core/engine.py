import time
import yaml
from urllib.parse import urljoin

from src.core.request import fetch
from src.core.loader import load_parser, load_exporter


def run(config_path):
    start_time = time.time()

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    parser = load_parser(config["parser"])
    exporter = load_exporter(config["exporter"])

    url = config["base_url"]
    all_data = []

    print("\n========================================")
    print("🚀 SCRAPING STARTED")
    print(f"Source: {config['base_url']}")
    print(f"Parser: {config['parser']}")
    print(f"Exporter: {config['exporter']}")
    print("========================================\n")

    page = 1

    while url:
        html = fetch(url, config["retries"], config["delay"])

        if not html:
            break

        items, next_url = parser(html, url)

        all_data.extend(items)

        print(f"📄 Page {page} scraped ({len(items)} items)")
        page += 1

        url = urljoin(url, next_url) if next_url else None

    exporter(all_data, config["output"])

    elapsed = round(time.time() - start_time, 2)

    print("\n========================================")
    print("✅ SCRAPING COMPLETED SUCCESSFULLY")
    print(f"📦 Total items scraped: {len(all_data)}")
    print(f"💾 Output file: {config['output']}")
    print(f"⏱ Time: {elapsed}s")
    print("========================================\n")