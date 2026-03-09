import json
from pathlib import Path

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE_DIR = Path(__file__).parent

def to_base62(num: int) -> str:
    result = []
    while num > 0:
        result.append(BASE62[num % 62])
        num //= 62
    return ''.join(reversed(result))

def shorten_urls() -> str:
    with open(BASE_DIR / "urls.json") as f:
        data = json.load(f)
    store = {to_base62(v["id"]): v["url"] for v in data.values()}
    return json.dumps(store)

