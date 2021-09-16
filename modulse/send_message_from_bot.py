import time
import telebot
from data.config import BOT_TOKEN

my_id = 716720991
vya_id = 1040471843

bot = telebot.TeleBot(BOT_TOKEN)

def send_message_from_bot(message: str):
    bot.send_message(my_id, message)
    bot.send_message(vya_id, message)
    time.sleep(0.5)