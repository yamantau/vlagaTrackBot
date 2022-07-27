tink_usd_rub = -1

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
            if marketdata.last_price is None:
                tink_usd_rub = 'Биржа закрыта'
            else:
                tink_usd_rub = 'usd/rub - ' + str(marketdata.last_price)

tinkoff_exchange = Thread(target=main, args=())