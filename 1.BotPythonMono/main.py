import time
from datetime import datetime
import schedule
import monobank
import telebot

chat_id = ''
bot = telebot.TeleBot('')

def start(message):
    today_ = datetime.today()
    bot.send_message(chat_id, str(mono_amount(datetime.date(today_), datetime.date(today_))) + " грн.")

def mono_amount(date1, date2):
    token = ''
    mono = monobank.Client(token)

    get_state1 = mono.get_statements('', date1, date2)
    allamount1=0
    for elem in get_state1:
        allamount1 = allamount1 + elem['amount']

    return int(allamount1 / 100)

    schedule.every(60).minutes.do(start)

    while True:
        schedule.run_pending()
        time.sleep(1)
