#tink_usd_rub

import time
import config
from threading import Thread
import data_saver

from tinkoff.invest import (
    CandleInstrument,
    Client,
    MarketDataRequest,
    SubscribeCandlesRequest,
    SubscriptionAction,
    SubscriptionInterval,
)

TOKEN = config.TINK_INVEST_TOKEN

def main():

    def get_rate_ex_tink():

        try:
            def request_iterator():
                yield MarketDataRequest(
                    subscribe_candles_request=SubscribeCandlesRequest(
                        waiting_close=True,
                        subscription_action=SubscriptionAction.SUBSCRIPTION_ACTION_SUBSCRIBE,
                        instruments=[
                            CandleInstrument(
                                figi=config.TINK_FIGI_USD_RUB,
                                interval=SubscriptionInterval.SUBSCRIPTION_INTERVAL_ONE_MINUTE,
                            )
                        ],
                    )
                )
                while True:
                    time.sleep(1)


            with Client(TOKEN) as client:
                for marketdata in client.market_data_stream.market_data_stream(
                    request_iterator()
                ):

                    if marketdata.candle is not None:

                        if len(str(marketdata.candle.close.nano)) < 9:
                            i = 9 - len(str(marketdata.candle.close.nano))
                            tink_usd_rub = float(str(marketdata.candle.close.units) + '.' + str(i*'0') + str(marketdata.candle.close.nano))
                            data_saver.rate_exchange_save(tink_usd_rub, 'usd_rub')

                        else:
                            tink_usd_rub = float(str(marketdata.candle.close.units) + '.' + str(marketdata.candle.close.nano))
                            data_saver.rate_exchange_save(tink_usd_rub, 'usd_rub')

                        exchange_is_open = True

                    else:
                        exchange_is_open = False

                    data_saver.info_update(exchange_is_open, 'usd_rub')

        except Exception as e:
            print(e)
            time.sleep(5)
            get_rate_ex_tink()

    tinkoff_exchange = Thread(target=get_rate_ex_tink, args=())

    tinkoff_exchange.start()