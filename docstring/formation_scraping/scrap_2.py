import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
response = requests.get(url)
url_category_base = "https://books.toscrape.com/catalogue/category"

with open("index.html", "w") as f:
    f.write(response.text)

with open("index.html", "r") as f:
    html = f.read()

limit = int(input("Entrez la limite choisie : "))
soup = BeautifulSoup(html, "html.parser")
aside = soup.find("div", class_="side_categories")
if aside != None:
    liste = aside.find("ul").find("li").find("ul").find_all("a")  # type: ignore
    for a in liste:
        url_category: str = a.get("href")
        url_category = url_category.replace("..", url_category_base)
        page_category = requests.get(url_category)
        page_category_content = BeautifulSoup(page_category.text, "html.parser")
        form = page_category_content.find("form", class_="form-horizontal")
        if form != None:
            quantity = form.find("strong")
            if quantity != None:
                quantity = int(quantity.text)  # type: ignore
                if quantity < limit:
                    category_name = page_category_content.find(
                        "div", class_="page-header action"
                    )
                    if category_name != None:
                        category_name = category_name.find("h1")
                        category_name = category_name.text  # type: ignore
                        print(
                            "La catégorie ",
                            category_name,
                            " compte moins de ",
                            limit,
                            " ouvrages.",
                        )
