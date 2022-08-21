import bin_p2p_parser
import tg_bot
import tink_parser
import spred_checker

bin_p2p_parser.main()
tink_parser.main()

tg_bot.tg_bot.start()

spred_checker.spred_tink_bin_p2p_check.start()
tg_bot.tg_bot_spammer.start()
