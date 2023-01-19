import random
import requests, datetime
import telebot
from telebot import types
from user_agent import generate_user_agent
from flask import request, Flask
from config import *
import os
import logging
# بسم اللَّه الرحمن الرحيم
# ممنوع خمط الملفات او نسخ الاكواد مامبري الذمة!

server = Flask(__name__)
spx = telebot.TeleBot(BOT_TOKEN)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
@spx.message_handler(commands=["start"])
def spyrx(message):
    idd = message.from_user.id
    message1 = message.text
    if idd != sudo_id:
        if message1 == "/start":
            spx.delete_message(message_id=message.chat.id, chat_id=message.chat.id)
    else:
        mb = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="يوزرات ثلاثية", callback_data="three_user")
        b2 = types.InlineKeyboardButton(text="يوزرات ثلاثية برقم", callback_data="three_user2")
        b3 = types.InlineKeyboardButton(text="المطور", url="t.me/h_69053")
        mb.row_width = 2
        mb.add(b1,b2,b3)
        mes = """
اهلًا بك في بوت صيد يوزرات تليجرام!
يمكنك التحكم عبر الازرار 

المطور ~ @h_69053        
        
        """
        spx.send_message(message.chat.id,text=mes,reply_markup=mb)
@spx.callback_query_handler(func=lambda call:True)
def sspyrx(call):
    if call.message:
        if call.data == 'three_user':
            bad = 0
            good = 0
            sb = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text=f"{bad} : ❌ عدد الغير المتاح", callback_data="none")
            b2 = types.InlineKeyboardButton(text=f"{good} : ✅ عدد المتاح ", callback_data="none")
            b3 = types.InlineKeyboardButton(text="المطور .", url="t.me/h_69053")
            sb.row_width = 2
            sb.add(b1,b2,b3)
            spx.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=sb)
            word = "pqwoeirutyalskdjfhgbvncmxz0164378240"
            w1 = random.choice(word)
            w2 = random.choice(word)
            w3 = random.choice(word)
            all = w1+"_"+w2+"_"+w3
            # ممنوع خمط الملفات او نسخ الاكواد مامبري الذمة!

            while True: 
                
                url = "https://t.me/"+all
                headers = {
                            "User-Agent": generate_user_agent(),
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                            "Accept-Encoding": "gzip, deflate, br",
                            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
                response = requests.get(url, headers=headers)
                if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
                    sb = types.InlineKeyboardMarkup()
                    b1 = types.InlineKeyboardButton(text=f"{bad} :❌ عدد الغير المتاح", callback_data="none")
                    b2 = types.InlineKeyboardButton(text=f"{good} :✅عدد المتاح ", callback_data="none")
                    b3 = types.InlineKeyboardButton(text="المطور .", url="t.me/h_69053")
                    sb.row_width = 2
                    sb.add(b1,b2,b3)
                    spx.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=sb)
                    msg2 = f"""
New User..
======================
User => {all}
Time => {datetime.now()}
======================
BY ~ @h_69053           
                    """
                    good += 1
                    spx.send_message(call.chat.id, msg2)
                else:
                    bad += 1
                    sbb = types.InlineKeyboardMarkup()
                    b5 = types.InlineKeyboardButton(text=f"{bad} :❌ عدد الغير المتاح", callback_data="none")
                    b6 = types.InlineKeyboardButton(text=f"{good} :✅عدد المتاح ", callback_data="none")
                    b7 = types.InlineKeyboardButton(text="المطور .", url="t.me/h_69053")
                    sbb.row_width = 2
                    sbb.add(b5,b6,b7)
                    spx.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=sbb)
        if call.data == 'three_user2':
            bad1 = 0
            good1 = 0
            sb = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text=f"{bad1} :❌ عدد الغير المتاح", callback_data="none")
            b2 = types.InlineKeyboardButton(text=f"{good1} :✅عدد المتاح ", callback_data="none")
            b3 = types.InlineKeyboardButton(text="المطور .", url="t.me/h_69053")
            sb.row_width = 2
            sb.add(b1,b2,b3)
            spx.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=sb)
            while True:    
                word = "pqwoeirutyalskdjfhgbvncmxz0164378240"
                number = "0987654321"
                w1 = random.choice(word)
                w2 = random.choice(word)
                w3 = random.choice(word)
                n1 = random.choice(number)
                al1l = w1+"_"+n1+"_"+w3
                # ممنوع خمط الملفات او نسخ الاكواد مامبري الذمة
                url = "https://t.me/"+al1l
                response = requests.get(url).status_code
                if response == 404:
                    sb = types.InlineKeyboardMarkup()
                    b1 = types.InlineKeyboardButton(text=f"{bad} :❌ عدد الغير المتاح", callback_data="none")
                    b2 = types.InlineKeyboardButton(text=f"{good} :✅عدد المتاح ", callback_data="none")
                    b3 = types.InlineKeyboardButton(text="المطور .", url="t.me/h_69053")
                    sb.row_width = 2
                    sb.add(b1,b2,b3)
                    spx.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=sb)
                    msg2 = f"""
New User..
======================
User => {al1l}
Time => {datetime.now()}
======================
BY ~ @h_69053           
                    """
                    good1 += 1
                    spx.send_message(call.chat.id, msg2)
                else:
                    bad1 += 1
                    sbb = types.InlineKeyboardMarkup()
                    b5 = types.InlineKeyboardButton(text=f"{bad1} :❌ عدد الغير المتاح", callback_data="none")
                    b6 = types.InlineKeyboardButton(text=f"{good1} :✅عدد المتاح ", callback_data="none")
                    b7 = types.InlineKeyboardButton(text="المطور .", url="t.me/h_69053")
                    sbb.row_width = 2
                    sbb.add(b5,b6,b7)
                    spx.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=sbb)
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    spx.process_new_updates([update])
    return "!", 200

if __name__ == "main":
    spx.remove_webhook()
    spx.set_webhook(url="https://mikalwkkwkqkq.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


# والحمدلله
# ممنوع خمط الملفات او نسخ الاكواد مامبري الذمة!



