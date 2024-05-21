import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article", class_="product_pod")
for article in articles:
    link = article.find_all("a")[1]
    print(link.get("title"))
