import logging
from random import randint
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from loguru import logger

def parse_olx(link):
    ua = UserAgent()

    headers = {
        "User-Agent": ua.random
    }
    logger.info(headers)
    # link = "https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/?search%5Border%5D=created_at%3Adesc"
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")

    offer_table = soup.find_all("table", {'id': 'offers_table'})

    links = []
    try:
        for _g in offer_table:
            for g in _g.find_all('div', {'class': 'offer-wrapper'}):
                link_element = g.find_all("a", {'class': 'link'})
                link = link_element[0]['href']

                text_title = link_element[0].find("strong").getText()


                if filter_ram(text_title.lower()):
                    continue

                links.append(link)
    except Exception as ex:
        logger.error(f"[OLX]: Error with parsing!")
    return links

def filter_ram(text):
    filter_words = [
        "ddr2",
        "ddr1",
        "ddr 2",
        "ddr 1",
        "ddr-2",
        "ddr-1"
    ]
    for i in filter_words:
        if i in text:
            return True
    return False
