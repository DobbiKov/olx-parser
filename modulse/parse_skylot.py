from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from loguru import logger

def parse_skylot(link):
    ua = UserAgent()

    headers = {
        "User-Agent": ua.random
    }
    logger.info(headers)
    # link = "https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/?search%5Border%5D=created_at%3Adesc"
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")

    rsearch = soup.find_all("div", {'class': 'rsearch'})
    # offers = soup.find_all("div", {'id': "j-bbs-search-list"})

    links = []
    try:
        for g in rsearch[0].find_all("div", {'class': 'search_lot'}):
            
            a = g.find("a")['href']
            links.append("https://skylots.org" + a)
    except Exception as ex:
        print(ex)
        logger.error(f"[SKYLOT]: Error with parsing!")
    
    return links
    # print(soup)
    # with open("./index.html", "w") as file:
    #     file.write(str(soup))