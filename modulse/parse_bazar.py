from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from loguru import logger

def parse_bazar(link):
    ua = UserAgent()

    headers = {
        "User-Agent": ua.random
    }
    logger.info(headers)
    # link = "https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/?search%5Border%5D=created_at%3Adesc"
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")
    offers = soup.find_all("div", {'id': "j-bbs-search-list"})

    links = []
    try:
        for g in offers[0].find_all("div", {'class': 'sr-2-list-item-n-in'}):
            divA = g.find("div", {'class': 'sr-2-list-item-n-title'})
            a = divA.find("a")['href']
            links.append(a)
    except Exception as ex:
        logger.error(f"[BAZAR]: Error with parsing!")
    
    return links
    # print(soup)
    # with open("./index.html", "w") as file:
    #     file.write(str(soup))