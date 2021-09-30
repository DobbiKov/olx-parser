from modulse.check_db_file import check_db_file
from modulse.parse_skylot import parse_skylot
from modulse.parse_promua import parse_promua
from modulse.parse_besplatka import parse_besplatka
from modulse.parse_bazar import parse_bazar
import time
from modulse.parse_olx_file import parse_olx_file
from modulse.send_email import send_email
from modulse.parse import parse
from loguru import logger
import random

logger.add('./logging/debug.txt', format="{time} {level} {message}", level="DEBUG") 

def main():
    check_db_file()
    logger.info("APP STARTED!")
    while True:
        parse()
        time.sleep(random.randint(240, 300))

if __name__ == "__main__":
    main()