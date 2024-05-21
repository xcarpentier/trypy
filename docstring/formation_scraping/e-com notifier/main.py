import requests
from selectolax.parser import HTMLParser


def main(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    html_content = response.text

    with open("amazon.html", "w") as f:
        f.write(html_content)

    tree = HTMLParser(html_content)
    price = tree.css_first("span.a-price-whole")
    return price


if __name__ == "__main__":
    asin = "B09QMG6FZX"
    url = f"https://www.amazon.fr/dp/B09QMG6FZX"
    main(url=url)
