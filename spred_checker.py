import data_loader
import time
from threading import Thread
import data_saver


def invset_tink_spred_saver():
    while True:

        tink_invest_spred = round((data_loader.get_rate_binance('p2p_usdt_rub_buy') / data_loader.get_exchange_rate('usd_rub') / data_loader.get_rate_binance('p2p_usdt_usd_buy') - 1.0) * 100 - 0.2, 2)
        data_saver.save_spred('invest_tink', tink_invest_spred)
        time.sleep(5)

spred_tink_bin_p2p_check = Thread(target=invset_tink_spred_saver, args=())


def spred_info():
    data_res = data_loader.get_spred()
    data_to_send = ''

    for item in data_res:
        data_to_send += 'Спред на ' + str(item['name']) + ': '+str(item['spred']) + '%\n'

    return data_to_send
