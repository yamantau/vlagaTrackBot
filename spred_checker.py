import time

import tinkoff_rate_exchange
import binance_p2p_parser
from threading import Thread

tink_invest_spred = -1.0
tink_invest_alarm = False

def invset_tink_check():
    while True:
        global tink_invest_spred
        tink_invest_spred = round((binance_p2p_parser.p2p_usdt_rub/tinkoff_rate_exchange.tink_usd_rub/binance_p2p_parser.p2p_usdt_usd-1.0)*100, 2)
        if tink_invest_spred > 0.1:
            global tink_invest_alarm
            tink_invest_alarm = True
        else:
            tink_invest_alarm = False
        time.sleep(5)

spred_tink_bin_p2p_check = Thread(target=invset_tink_check, args=())

