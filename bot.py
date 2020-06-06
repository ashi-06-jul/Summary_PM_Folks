import time
import telebot
from db import DB
import sqlite3

TOKEN = "bot_token"
bot = telebot.TeleBot(token=TOKEN)
hire=""
new_technology="" 
good_conversations="" 
doubts=""
upcoming_events=""
def findat(msg):
    # from a list of texts, it finds the one with the '#' sign
    for i in msg:
        if '#' in i:
            return i

def db(message):
    db = DB()
    db.setup()
    db.add_item(
		message.chat.text["hire"], 
		message.chat.text["new_technology"], 
		message.chat.text["good_conversations"], 
        message.chat.text["doubts"],
		message.chat.text["upcoming_events"])

@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, '(placeholder text)')

@bot.message_handler(commands=['help']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'ALPHA = FEATURES MAY NOT WORK')

@bot.message_handler(func=lambda msg: msg.text is not None and '#' in msg.text)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '#': # in case it's just the '#', skip
        pass
    elif at_text == '#hire':
        #insta_link = "https://instagram.com/{}".format(at_text[1:])
        hire = "Hiring Conversation"
        bot.reply_to(message,hire)
    elif at_text == '#new_technology':
        new_technology = "New Technology"
        bot.reply_to(message, new_technology)
    elif at_text == '#good_conversations':
        good_conversations = "Good Conversations"
        bot.reply_to(message, good_conversations)
    elif at_text == '#doubts':
        doubts = "Doubts".format(at_text[1:])
        bot.reply_to(message, doubts)
    elif at_text == '#upcoming_events':
        upcoming_events = "Upcoming Events"
        bot.reply_to(message, upcoming_events)
    elif at_text == '#end':
        db(message)
        end = "Okay bbyee"
        bot.reply_to(message, end)
    else:
        insta_link = "https://instagram.com/{}".format(at_text[1:])
        bot.reply_to(message, insta_link)



while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(5)
