from threading import Thread
import telebot
import time
import config
import data_loader
import data_saver
import graph_maker
import spred_checker

bot = telebot.TeleBot(config.TG_BOT_TOKEN)

def tg_bot_start():

    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        time.sleep(1)
        bot.send_message(m.chat.id, 'Привет, это vlaga track bot\. \n\nНапиши /help, чтобы посмотреть все команды, твой id: '
                                    + '`' +str(m.chat.id) + '`', parse_mode='MarkdownV2')

    @bot.message_handler(commands=["usd_rub"])
    def start(m, res=False):
        time.sleep(1)

        auth_res = data_loader.check_auth_user(m.chat.id, config.USER)

        if auth_res is True:

            data_res = data_loader.get_exchange_rate('usd_rub')
            bot.send_message(m.chat.id, 'Курс usd/rub - ' + str(data_res))

        else:
            bot.send_message(m.chat.id, auth_res)

    @bot.message_handler(commands=["bin_p2p_usdt_usd"])
    def start(m, res=False):
        time.sleep(1)

        auth_res = data_loader.check_auth_user(m.chat.id, config.USER)

        if auth_res is True:

            data_res = data_loader.get_rate_binance('p2p_usdt_usd_buy')
            bot.send_message(m.chat.id, 'Курс usdt/usd - ' + str(data_res))

        else:
            bot.send_message(m.chat.id, auth_res)

    @bot.message_handler(commands=["bin_p2p_usdt_rub"])
    def start(m, res=False):
        time.sleep(1)

        auth_res = data_loader.check_auth_user(m.chat.id, config.USER)

        if auth_res is True:

            data_res = data_loader.get_rate_binance('p2p_usdt_rub_buy')
            bot.send_message(m.chat.id, 'Курс usdt/rub - ' + str(data_res))

        else:
            bot.send_message(m.chat.id, auth_res)

    @bot.message_handler(commands=["help"])
    def start(m, res=False):
        time.sleep(1)
        bot.send_message(m.chat.id, 'Команды, которые сейчас доступны:\n\n'
                                    '/spred - Инфа по спреду \n\n'
                                    'Инфа по курсам: \n'
                                    
                                    '/bin_p2p_usdt_usd - Курс usdt/usd p2p bin \n'
                                    '/bin_p2p_usdt_rub - Курс usdt/rub p2p bin \n\n'
                                    
                                    '/usd_rub - Курс usd/rub \n\n'
        # '/invest - Тиньк инвест\n\n'
                                    'Инструменты: \n'
                                    '/graph_usdt_rub минуты - График p2p bin usdt/rub\n'
                                    '/graph_usdt_usd минуты- График p2p bin usdt/usd')

        if data_loader.check_auth_user(m.chat.id, config.ADMIN) is True:
            time.sleep(1)
            bot.send_message(m.chat.id, 'Админ панель:\n\n'
                                        '/add id - добавить человека\n'
                                        '/updsub id - продлить подписку')


    @bot.message_handler(commands=["spred"])
    def start(m, res=False):
        time.sleep(1)

        auth_res = data_loader.check_auth_user(m.chat.id, config.USER)

        if auth_res is True:

            bot.send_message(m.chat.id, spred_checker.spred_info())

        else:

            bot.send_message(m.chat.id, auth_res)

    @bot.message_handler(commands=["add"])
    def start(m, res=False):

        auth_res = data_loader.check_auth_user(m.chat.id, config.ADMIN)

        if auth_res is True:

            message = m.text.split(' ')[1]

            try:
                data_saver.add_user(message)
                time.sleep(1)
                bot.send_message(m.chat.id, 'Добавил')
            except Exception as e:
                print(e)
                time.sleep(1)
                bot.send_message(m.chat.id, 'Не получилось')

        else:

            bot.send_message(m.chat.id, auth_res)

    @bot.message_handler(commands=["updsub"])
    def start(m, res=False):

        auth_res = data_loader.check_auth_user(m.chat.id, config.ADMIN)

        if auth_res is True:

            message = int(m.text.split(' ')[1])

            try:
                data_saver.update_subscribe(message)
                time.sleep(1)
                bot.send_message(m.chat.id, 'Продлил')
            except Exception as e:
                print(e)
                time.sleep(1)
                bot.send_message(m.chat.id, 'Не получилось')

        else:

            bot.send_message(m.chat.id, auth_res)


    @bot.message_handler(commands=["graph_usdt_rub"])
    def start(m, res=False):

        auth_res = data_loader.check_auth_user(m.chat.id, config.USER)

        if auth_res is True:

            try:
                message = m.text.split(' ')[1]

                try:
                    message = int(message)

                    try:
                        graph_maker.make_graph(int(message), 'p2p_usdt_rub')
                        graph = open('my_figure_file.png', 'rb')
                        bot.send_photo(m.chat.id, graph, caption='')
                    except Exception as e:
                        print(str(e) + ' Построение графика')
                        bot.send_message(m.chat.id, 'Пока что не хватает значений, введи значения меньше')

                except Exception as e:
                    bot.send_message(m.chat.id, 'Нужны числа')

            except Exception as e:
                bot.send_message(m.chat.id, 'Нужен формат "/команда минуты". \nПример: /graph_usdt_rub 230')

        else:
            bot.send_message(m.chat.id, auth_res)

    @bot.message_handler(commands=["graph_usdt_usd"])
    def start(m, res=False):

        auth_res = data_loader.check_auth_user(m.chat.id, config.USER)

        if auth_res is True:

            try:
                message = m.text.split(' ')[1]

                try:
                    message = int(message)

                    try:
                        graph_maker.make_graph(int(message), 'p2p_usdt_usd')
                        graph = open('my_figure_file.png', 'rb')
                        bot.send_photo(m.chat.id, graph, caption='')
                    except Exception as e:
                        print(str(e) + ' Построение графика')
                        bot.send_message(m.chat.id, 'Пока что не хватает значений, введи значения меньше')

                except Exception as e:
                    bot.send_message(m.chat.id, 'Нужны числа')

            except Exception as e:
                bot.send_message(m.chat.id, 'Нужен формат "/команда минуты". \nПример: /graph_usdt_rub 230')

        else:
            bot.send_message(m.chat.id, auth_res)

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

        data_res = data_loader.get_spred()
        data_to_send = ''

        for item in data_res:
            if item['spred'] > 0 and data_loader.get_info('is_exchange_open'):
                data_to_send += 'Спред на ' + str(item['name']) + ': '+str(item['spred']) + '%\n'

        if data_to_send == '':
            data_to_send = 'Спреда нет'
        else:
            bot.send_message(config.TG_BOT_MY_ID, data_to_send)
            # bot.send_message(config.TG_BOT_KURBATOV_ID, data_to_send)

        time.sleep(600)

tg_bot_spammer = Thread(target=auto_spam, args=())