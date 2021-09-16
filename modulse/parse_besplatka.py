from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from loguru import logger

def parse_besplatka(link):
    ua = UserAgent()

    headers = {
        "User-Agent": ua.random
    }
    logger.info(headers)
    # link = "https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/?search%5Border%5D=created_at%3Adesc"
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")
    offers = soup.find_all("div", {'class': "messages-list"})

    links = []
    try:
        for g in offers[0].find_all("div", {'class': 'msg-one'}):
            # divA = g.find("div", {'class': 'sr-2-list-item-n-title'})
            a = g.find("a", {'class': 'm-title'})['href']
            links.append("https://besplatka.ua" + a)
    except Exception as ex:
        logger.error(f"[BESPLATKA]: Error with parsing!")

    return links
    # print(soup)
    # with open("./index.html", "w") as file:
    #     file.write(str(soup))