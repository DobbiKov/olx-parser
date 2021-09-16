import smtplib
import os
from loguru import logger
from data.config import EMAIL_PASSWORD


def send_email(message: str, to: str, title=""):
    sender = "apanikaxi@gmail.com"
    password = EMAIL_PASSWORD

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender, password)
        server.sendmail(sender, to, f"Subject: {title}\n{message}")
    except Exception as ex:
        logger.error("CAN'T SEND EMAIL!")
        print(ex)