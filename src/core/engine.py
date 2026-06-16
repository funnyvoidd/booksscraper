import yaml
from urllib.parse import urljoin

from src.core.request import fetch
from src.core.loader import load_parser, load_exporter

def run(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    parser = load_parser(config["parser"])
    exporter = load_exporter(config["exporter"])

    url = config["base_url"]
    all_data = []

    while url:
        html = fetch(url, config["retries"], config["delay"])
        if not html:
            break

        items, next_url = parser(html, url)
        all_data.extend(items)

        url = urljoin(url, next_url) if next_url else None

    exporter(all_data, config["output"])

    print("\n" + "=" * 50)
    print("✅ SCRAPING COMPLETED SUCCESSFULLY")
    print(f"📦 Total items scraped: {len(all_data)}")
    print(f"💾 Results saved to: {config['output']}")
    print("=" * 50 + "\n")