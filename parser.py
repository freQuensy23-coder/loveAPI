import requests as req
from bs4 import BeautifulSoup as BS
import logging

log = logging.getLogger("parser")


def get_page_link(link, page_num):
    log.debug(f"Ger page link to {link} and {page_num}.")
    if page_num == 1:
        log.debug(f"Get {link}")
        return link
    if link[-1] == "/":
        log.debug(f'Get {link[:-1] + f"_{page_num}"}')
        return link[:-1] + f"{page_num}"
    else:
        log.debug(f'Get {link + f"{page_num}"}')
        return link + f"{page_num}"


def get_page_msgs(page: bytes) -> list:
    """Returns list of str - sms on page page"""
    soup = BS(page, "lxml")
    msgs = soup.find_all("p", {"class": "nth2"})
    for i, msg in enumerate(msgs):
        msgs[i] = msg.text
    return msgs


def get_group_msgs(link: str) -> list:
    """:param link - url to the first page of this group"""
    i = 1
    msgs = []
    r = req.get(get_page_link(link=link, page_num=i))
    while r.status_code == 200:
        msgs.append(get_page_msgs(r.content))
        i += 1
        r = req.get(get_page_link(link=link, page_num=i))
    return msgs
