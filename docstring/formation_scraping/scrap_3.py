import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)

# with open("index.html", "w") as f:
#    f.write(response.text)
#
# with open("index.html", "r") as f:
#    html = f.read()

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article", class_="product_pod")
if articles != None:
    for article in articles:
        star_rating = article.find("p", class_="star-rating")
        if star_rating != None:
            number_of_star = star_rating.get("class")[1]
            if number_of_star == "One":
                h3 = article.find("h3")
                if h3 != None:
                    a = h3.find("a")
                    if a != None:
                        name_of_book = a.get("title")
                        if name_of_book != None:
                            book_link: str = a.get("href")
                            index_underscore = int(book_link.find("_"))
                            index_slash = int(book_link.find("/"))
                            book_ID = book_link[index_underscore + 1 : index_slash]
                            print(
                                f"Le livre {name_of_book} dont l'identifiant est {book_ID} n'a q'une seule étoile."
                            )
                        else:
                            book_link: str = a.get("href")
                            index_underscore = int(book_link.find("_"))
                            index_slash = int(book_link.find("/"))
                            book_ID = book_link[index_underscore + 1 : index_slash]
                            print(
                                f"Le livre dont l'identifiant est {book_ID} n'a q'une seule étoile. Il y a un problème avec son titre."
                            )
                    else:
                        a = article.find("div", class_="image_container")
                        image_link = str(a.get("href"))
                        short_link = image_link[6:-1]
                        index_underscore = int(short_link.find("_"))
                        name_of_book = short_link[0:index_underscore]
                        index_slash = int(short_link.find("/"))
                        book_ID = short_link[index_underscore + 1 : index_slash]
                        print(
                            f"Le livre {name_of_book} dont l'identifiant est {book_ID} a un problème avec son lien."
                        )
                else:
                    index_underscore = int(book_link.find("_"))
                    index_slash = int(book_link.find("/"))
                    book_ID = book_link[index_underscore + 1 : index_slash]
                    print(
                        f"Il y a un problème avec le h3 qui contient le titre du livre dont l'identifiant est {book_ID}"
                    )
        else:
            h3 = article.find("h3")
            a = h3.find("a")
            name_of_book = a.get("title")
            book_link: str = a.get("href")
            index_underscore = int(book_link.find("_"))
            index_slash = int(book_link.find("/"))
            book_ID = book_link[index_underscore + 1 : index_slash]
            print(
                f"Le livre {name_of_book} d'identifiant {book_ID} a un problème avec les avis."
            )
