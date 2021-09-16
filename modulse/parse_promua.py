from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from loguru import logger
from lxml import etree

def parse_promua(link):
    ua = UserAgent()

    headers = {
        "User-Agent": ua.random
    }
    logger.info(headers)
    # link = "https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/?search%5Border%5D=created_at%3Adesc"
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")
    dom = etree.HTML(str(soup))

    offers = (dom.xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/a'))
    # nalichie = (dom.xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/span/span/text()'))
    # print(nalichie)

    links = []
    try:
        for i in offers:
            links.append("https://prom.ua" + i.attrib['href'].split(".html")[0] + ".html")
    except Exception as ex:
        logger.error(f"[PROM-UA]: Error with parsing!")
        
    return links

    
    # print(soup)
    # with open("./index.html", "w") as file:
    #     file.write(str(soup))