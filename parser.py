import requests as req
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging

log = logging.getLogger("parser")


def get_page_link(link, page_num):
    log.debug(f"Ger page link to {link} and {page_num}.")
    if link[-1] == "/":
        log.debug(f'Get {link[:-1] + f"_{page_num}"}')
        return link[:-1] + f"{page_num}"
    else:
        log.debug(f'Get {link + f"{page_num}"}')
        return link + f"{page_num}"

