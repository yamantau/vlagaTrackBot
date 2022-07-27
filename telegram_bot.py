from threading import Thread
import telebot
import tinkoff_rate_exchange

def tg_bot_start():


    bot = telebot.TeleBot('5309307055:AAFqSpFNs5ZlIS-emzjTursAp9cH8MmJAnI')

    @bot.message_handler(commands=["help"])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'Привет, это vlaga track bot. \n\nКоманды, которые сейчас доступны: \n/help - все команды \n/gcusd - курс usd/rub')

    @bot.message_handler(commands=["gcusd"])
    def start(m, res=False):
        bot.send_message(m.chat.id, tinkoff_rate_exchange.tink_usd_rub)

    bot.polling(none_stop=True, interval=0)

tg_bot = Thread(target=tg_bot_start, args=())