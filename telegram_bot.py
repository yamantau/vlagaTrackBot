from threading import Thread
import telebot
import tinkoff_rate_exchange
import time
import binance_p2p_parser
import config
import spred_checker

bot = telebot.TeleBot('5309307055:AAFqSpFNs5ZlIS-emzjTursAp9cH8MmJAnI')

def tg_bot_start():

    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'Привет, это vlaga track bot. \n\nНапиши /help, чтобы посмотреть все команды ')

    @bot.message_handler(commands=["help"])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'Команды, которые сейчас доступны:\n\n'
                                    'Инфа по курсам: \n'
                                    '/tinkusdrub - курс usd/rub \n'
                                    '/binp2pusdtusd - курс usdt/usd p2p bin \n'
                                    '/binp2pusdtrub - курс usdt/rub p2p bin \n\n'
                                    'Инфа по спреду: \n'
                                    '/invest - тиньк инвест')

    @bot.message_handler(commands=["tinkusdrub"])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'usd/rub tink - ' + str(tinkoff_rate_exchange.tink_usd_rub))
        print(m.chat.id)

    @bot.message_handler(commands=["binp2pusdtusd"])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'usdt/usd p2p bin tink - ' + str(binance_p2p_parser.p2p_usdt_usd))
        print(m.chat.id)

    @bot.message_handler(commands=["binp2pusdtrub"])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'usdt/rub p2p bin tink - ' + str(binance_p2p_parser.p2p_usdt_rub))
        print(m.chat.id)

    @bot.message_handler(commands=["invest"])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'Cпред на инвестициях: ' + str(spred_checker.tink_invest_spred) + '%')
        print(m.chat.id)


    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue

tg_bot = Thread(target=tg_bot_start, args=())


def auto_spam():
    while True:
        if spred_checker.tink_invest_alarm is True:
            bot.send_message(config.TG_BOT_MY_ID, 'Есть спред на инвестициях: ' + str(spred_checker.tink_invest_spred) + '%')
            bot.send_message(config.TG_BOT_KURBATOV_ID, 'Есть спред на инвестициях: ' + str(spred_checker.tink_invest_spred) + '%')
        time.sleep(10)

tg_bot_spammer = Thread(target=auto_spam, args=())