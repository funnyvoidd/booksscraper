import yaml
from core.request import fetch
from parsers.books_parser import parse
from exporters.csv_exporter import export_csv
from urllib.parse import urljoin

def run(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    url = config["base_url"]
    all_data = []

    while url:
        html = fetch(url, config["retries"], config["delay"])
        if not html:
            break

        items, next_url = parse(html, url)

        all_data.extend(items)

        url = urljoin(url, next_url) if next_url else None

    export_csv(all_data, config["output"])