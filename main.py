import telegram_bot
import tinkoff_rate_exchange
import binance_p2p_parser
import spred_checker

telegram_bot.tg_bot.start()
telegram_bot.tg_bot_spammer.start()
tinkoff_rate_exchange.tinkoff_exchange.start()
binance_p2p_parser.bin_p2p_usdt_usd.start()
binance_p2p_parser.bin_p2p_usdt_rub.start()
spred_checker.spred_tink_bin_p2p_check.start()
