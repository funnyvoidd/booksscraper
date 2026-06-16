import requests
import logging

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def safe_request(url, timeout=10):
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r
    except Exception as e:
        logging.error(f"Request error {url}: {e}")
        return None