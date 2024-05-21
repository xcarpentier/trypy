import sys
import requests
from pathlib import Path
from loguru import logger
from datetime import datetime
from selectolax.parser import HTMLParser
import json

logger.remove()
logger.add(sys.stderr, level="INFO")


PRICE_FILEPATH = Path(__file__).parent / "price.json"


def fetch_content(url: str, headers) -> HTMLParser:
    try:
        logger.info(f"Fetching content from page : {url}")
        response = requests.get(url=url, headers=headers)
        response.raise_for_status
    except requests.RequestException as e:
        logger.error(
            f"There was an error during the request of that url : {url} : {str(e)}"
        )
        raise e
    else:
        html_content = response.text
        print(html_content)
        tree = HTMLParser(html_content)
        return tree


def get_price(tree: HTMLParser):
    price_container = tree.css_first("span.info-data-price > span.txt-bold")
    price = int(price_container.text())
    return price


def write_price_to_file(price: int) -> None:
    if PRICE_FILEPATH.exists():
        with open(PRICE_FILEPATH, "r") as f:
            data = json.load(f)
    else:
        data = []
    data.append({"price": price, "timestamp": datetime.now().isoformat()})
    with open(PRICE_FILEPATH, "w") as f:
        json.dump(data, f, indent=4)


def get_price_difference(current_price: int) -> float:
    logger.info("Getting some price difference.")
    if PRICE_FILEPATH.exists():
        with open(PRICE_FILEPATH, "r") as f:
            data = json.load(f)
            previous_price = data[-1]["price"]
    else:
        previous_price = current_price
    price_difference = (current_price - previous_price) / previous_price * 100
    return price_difference


def main(url: str, headers):
    tree = fetch_content(url=url, headers=headers)
    price = get_price(tree=tree)
    write_price_to_file(price=price)
    price_difference = get_price_difference(current_price=price)
    if price_difference > 0:
        logger.info(f"Le prix a augmenté de {price_difference}%.")
    elif price_difference < 0:
        logger.info(f"Le prix a baissé de {price_difference}%.")


if __name__ == "__main__":
    url = "https://www.idealista.it/immobile/29683919/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    main(url=url, headers=headers)
