from modulse.parse_skylot import parse_skylot
from modulse.parse_promua import parse_promua
from modulse.parse_besplatka import parse_besplatka
from modulse.parse_bazar import parse_bazar
from modulse.parse_olx import parse_olx
from modulse.send_message_from_bot import send_message_from_bot
from modulse.send_email import send_email
from modulse.parse_olx_file import parse_olx_file
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from loguru import logger

def get_link_from_file(src):
    with open(src, "r") as file:
        return file.read()
def parse():
    # olx_neispravny_links = parse_olx(olx_neispravny_link)
    # olx_zalit_links = parse_olx(olx_zalit_link)
    skylot_links = parse_skylot(get_link_from_file("./links/skylot.txt"))
    bazar_links = parse_bazar(get_link_from_file("./links/bazar.txt"))
    besplatka_links = parse_besplatka(get_link_from_file("./links/besplatka.txt"))
    

    olx_ddr3_links = parse_olx(get_link_from_file("./links/olx_ddr3.txt"))
    olx_ddr4_links = parse_olx(get_link_from_file("./links/olx_ddr4.txt"))



    arrays_links = [
        # olx_neispravny_links, 
        # olx_zalit_links,

        skylot_links,
        olx_ddr3_links,
        olx_ddr4_links,
        bazar_links,
        besplatka_links,

        # promua_links
    ]

    links = []
    for i in arrays_links:
        links += i

    new_links = []
    links = list(set(links))
    

    for link in links:
        if link_handler(link) == True:
            new_links.append(link)
    send_links(new_links)

def link_handler(link: str):
    array = parse_olx_file("./parsed_links.txt")
    
    if link in array:
        # print("NOT")
        return False
    # print("YES")
    with open("./parsed_links.txt", "a") as file:
        file.write(link + ",,,")

    return True

def send_links(array):
    array = list(set(array))
    if len(array) == 0:
        return
    text = f"Новые объявления {len(array)}:"
    send_message_from_bot(text)

    for i in array:
        text = f"{i}"
        send_message_from_bot(text)
    # send_email(f"Новое объявление: {text}", "dobbikov@gmail.com", title="Новые объявления!")
    logger.info(f"Новые объявления!")
    