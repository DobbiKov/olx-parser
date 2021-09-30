import os

def check_db_file():
    if not os.path.exists("./parsed_links.txt"):
        with open("./parsed_links.txt", "w") as file:
            file.close