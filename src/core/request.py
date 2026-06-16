import requests
import time

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch(url, retries=3, delay=1):
    for i in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=10)
            r.raise_for_status()
            r.encoding = "utf-8"
            return r.text
        except Exception:
            time.sleep(delay * (2 ** i))
    return None