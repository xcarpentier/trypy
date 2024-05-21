import sys

import requests
from selectolax.parser import HTMLParser
from loguru import logger
from urllib.parse import urljoin
import re

logger.remove()
logger.add(f"books.log", level="WARNING", rotation="1024kb")
logger.add(sys.stderr, level="INFO")

BASE_URL = "https://books.toscrape.com/catalogue/category/books_1/page-1.html"
pages_urls_list = ["https://books.toscrape.com/catalogue/category/books_1/page-1.html"]
books_urls_list = []


# Fonction pour trouver l'url de chaque page
def get_page_url(tree: HTMLParser, url: str):
    url_a = tree.css_first("li.next > a")
    if url_a and url_a.attributes["href"]:
        page_url = urljoin(BASE_URL, url_a.attributes["href"])
        current_page_url = url
        logger.info(
            f"Récupération de l'url de la page suivante à celle-ci : {current_page_url} : {page_url}"
        )
        return page_url


# Fonction pour récupérer les urls de toutes les pages
def get_all_pages_urls(url: str):
    with requests.Session() as session:
        while True:
            try:
                response = session.get(url)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                logger.error(
                    f"Erreur lors de la récupération du fichier HTML de cette page : {url}"
                )
                break
            else:
                tree = HTMLParser(response.text)
                page_url = get_page_url(tree=tree, url=url)
                if page_url:
                    pages_urls_list.append(page_url)
                    url = page_url
                else:
                    logger.info("La récupération des urls des pages est terminée.")
                    break
        return pages_urls_list


# Fonction pour récupérer les urls de tous les livres d'une page
def get_all_books_urls_on_page(tree: HTMLParser, url: str):
    link_containers = tree.css("h3 > a")
    if link_containers:
        try:
            books_links = [
                urljoin(BASE_URL, link.attributes["href"]) for link in link_containers
            ]
        except KeyError as e:
            logger.error(
                f"Les balises 'a' des livres de la page {url} ne contiennent pas de balise 'href' : {e}"
            )
        else:
            logger.info(f"Récupération des urls des livres de cette page : {url}")
            return books_links


# Fonction pour récupérer tous les urls de tous les livres du site
def get_all_books_urls(url: str):
    pages_urls_list = get_all_pages_urls(url=url)
    with requests.Session() as session:
        for link in pages_urls_list:
            try:
                response = session.get(link)
                response.raise_for_status
            except requests.exceptions.RequestException as e:
                logger.error(
                    f"Il y a eu une erreur lors de la récupération du fichier HTML de la page {link}"
                )
            else:
                tree = HTMLParser(response.text)
                page_books_urls = get_all_books_urls_on_page(tree=tree, url=link)
                if page_books_urls:
                    books_urls_list.extend(page_books_urls)
        logger.info("La récupération des urls de tous les livres du site est terminée.")
        return books_urls_list


# Fonction pour trouver le prix unitaire d'un livre
def get_book_unit_price(tree: HTMLParser, url: str) -> float:
    try:
        price_container = tree.css_first("p.price_color").text()
    except AttributeError as e:
        logger.error(
            f"Il n'y a pas de 'p' de classe 'price_color' sur la page de ce livre : {url} : {e}"
        )
        return 0.0
    else:
        price = re.findall(r"[0-9.]+", price_container)[0]
        logger.info(f"Récupération du prix du livre {url} : {price}")
        return price


# Fonction pour trouver le nombre d'exemplaires en stock d'un livre
def get_book_stock(tree: HTMLParser, url: str) -> int:
    try:
        stock_container = tree.css_first("p.instock.availability").text()
    except AttributeError as e:
        logger.error(
            f"Il n'y a pas de 'p' de classes 'instock availability' sur la page de ce livre : {url} : {e}"
        )
        return 0
    else:
        stock = re.findall(r"[\d]+", stock_container)[0]
        logger.info(f"Récupération du stock du livre {url} : {stock}")
        return stock


# Fonction pour déterminer le prix du stock d'un livre
def get_stock_price(tree: HTMLParser, url: str) -> float:
    price = float(get_book_unit_price(tree=tree, url=url))
    stock = int(get_book_stock(tree=tree, url=url))
    stock_price = price * stock
    logger.info(f"Récupération du prix du stock du livre {url} : {stock_price}")
    return stock_price


def main(url: str) -> float:
    books_urls_list = get_all_books_urls(url=url)
    total_price = 0
    with requests.Session() as session:
        for link in books_urls_list:
            try:
                response = session.get(link)
                response.raise_for_status
            except requests.exceptions.RequestException as e:
                logger.error(
                    f"Il y a eu une erreur lors de la récupération du fichier HTML de la page {link} : {e}"
                )
            else:
                tree = HTMLParser(response.text)
                price_stock = get_stock_price(tree=tree, url=link)
                total_price = total_price + price_stock
        logger.info(
            f"Le prix total du stock de livres de la librairie est de {total_price}"
        )
        return total_price


if __name__ == "__main__":
    main(url=BASE_URL)
