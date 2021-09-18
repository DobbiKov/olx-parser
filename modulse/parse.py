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

# laptop: https://www.olx.ua/elektronika/noutbuki-i-aksesuary/?search%5Border%5D=created_at%3Adesc
olx_neispravny_link = "https://www.olx.ua/elektronika/noutbuki-i-aksesuary/noutbuki/q-%D0%BD%D0%B5%D0%B8%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9/?search%5Bfilter_float_price%3Ato%5D=2000&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_display_size%5D%5B0%5D=3#"
olx_zalit_link = "https://www.olx.ua/elektronika/noutbuki-i-aksesuary/noutbuki/q-%D0%B7%D0%B0%D0%BB%D0%B8%D1%82/?search%5Bfilter_float_price%3Ato%5D=2000&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_display_size%5D%5B0%5D=3"

olx_ddr4_link = "https://www.olx.ua/elektronika/noutbuki-i-aksesuary/noutbuki/q-ddr4/?search%5Bfilter_float_price%3Ato%5D=2000&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_display_size%5D%5B0%5D=3"
olx_ddr3_link = "https://www.olx.ua/elektronika/noutbuki-i-aksesuary/noutbuki/q-ddr3/?search%5Bfilter_float_price%3Ato%5D=2000&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_enum_display_size%5D%5B0%5D=3"

promua_link = "https://prom.ua/Noutbuki?price_local__lte=2000&a10006=83770&a1373__lte=16&a1373__gte=15&search_term=%D0%BD%D0%B5%D0%B8%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9&binary_filters=presence_available"
besplatka_link = "https://besplatka.ua/ru/electronika-i-bitovaya-tehnika/kompyutery-i-komplektuyushie/noutbuki/b-u/15-6-dyuimov?prop[2][to]=2000&currency=UAH"
# besplatka_neispravny_link = "https://besplatka.ua/ru/electronika-i-bitovaya-tehnika/kompyutery-i-komplektuyushie/noutbuki/b-u/15-6-dyuimov/q-%D0%BD%D0%B5+%D0%B8%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9?prop[2][to]=2000&currency=UAH"
# besplatka_zalit_link = "https://besplatka.ua/ru/electronika-i-bitovaya-tehnika/kompyutery-i-komplektuyushie/noutbuki/b-u/15-6-dyuimov/q-%D0%B7%D0%B0%D0%BB%D0%B8%D1%82?prop[2][to]=2000&currency=UAH"

bazarua_link = "https://bazar.ua/elektronika/kompyutery/noutbuki/?c=80&ct=0&lt=1&sort=new&page=1&q=&p%5Bf%5D=&p%5Bt%5D=2000&p%5Bc%5D=1&d%5B1%5D%5B%5D=3&d%5B2%5D%5B%5D=1"

skylot_link = "https://skylots.org/c111254/Noutbuki/?search=&desc_check=0&seller_id=0&new=0&ex=0&end_ex=0&price_from=&price_to=2000&items_from=&items_to=&city=&filters%5B%5D=716&filters%5B%5D=1095&filters%5B%5D=994083&catid=111254&orderby=7#?"
def parse():
    # olx_neispravny_links = parse_olx(olx_neispravny_link)
    # olx_zalit_links = parse_olx(olx_zalit_link)
    skylot_links = parse_skylot(skylot_link)
    bazar_links = parse_bazar(bazarua_link)
    besplatka_links = parse_besplatka(besplatka_link)
    promua_links = parse_promua(promua_link)

    olx_ddr3_links = parse_olx(olx_ddr3_link)
    olx_ddr4_links = parse_olx(olx_ddr4_link)



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
        print("NOT")
        return False
    print("YES")
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
    