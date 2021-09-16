from loguru import logger

def parse_olx_file(path):
    with open(path, "r") as file:
        file_string = file.read()

        array = file_string.split(",,,")
        return array