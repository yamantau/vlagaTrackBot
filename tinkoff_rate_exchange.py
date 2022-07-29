tink_usd_rub = -1
last_price_tink_usd_rub = -1

import time
import config
from threading import Thread

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

            global tink_usd_rub
            print(marketdata)
            global last_price_tink_usd_rub
            try:
                if marketdata is None:
                    tink_usd_rub = str(last_price_tink_usd_rub) + ', биржа закрыта'
                else:
                    tink_usd_rub = float(str(marketdata.candle.close.units) + '.' + str(marketdata.candle.close.nano).rstrip('0'))
                    last_price_tink_usd_rub = tink_usd_rub

            except Exception as e:
                print(e)
                time.sleep(5)
                continue

tinkoff_exchange = Thread(target=main, args=())