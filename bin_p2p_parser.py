from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time
from threading import Thread

import data_saver

URL_BINANCE_P2P_USDT_USD_BUY = "https://p2p.binance.com/ru/trade/Tinkoff/USDT?fiat=USD"
URL_BINANCE_P2P_USDT_USD_SELL = "https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payment=Tinkoff"
URL_BINANCE_P2P_USDT_RUB_BUY = "https://p2p.binance.com/ru/trade/Tinkoff/USDT?fiat=RUB"
URL_BINANCE_P2P_USDT_RUB_SELL = "https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payment=Tinkoff"
PATH_TO_WEBDRIVER = 'D:\proger\webdriver\chromedriver.exe'

def main():

    def rate_buy_usdt_usd():

        # Start driver
        driver = webdriver.Chrome(PATH_TO_WEBDRIVER)
        driver.get(URL_BINANCE_P2P_USDT_USD_BUY)

        try:
            time.sleep(5)

            # Lesson preview window with x
            driver.find_element(By.CLASS_NAME, "css-1pcqseb").click()

            # Mini pre-chat (right down)
            driver.find_element(By.CLASS_NAME, "css-1v60uza").click()

            # Fiat filter
            driver.find_element(By.CLASS_NAME, "css-1nlwvj5").click()
            driver.find_element(By.ID, "USD").click()
            time.sleep(5)

            # Merchant filter
            driver.find_element(By.CLASS_NAME, "css-5xw3l7").click()
            driver.find_element(By.CLASS_NAME, "css-l7x4y").click()
            time.sleep(5)

            # Update filter
            driver.find_element(By.CLASS_NAME, "css-qev57u").click()
            driver.find_element(By.XPATH, "//*[contains(text(), '5 с до обновления')]").click()
            time.sleep(5)

            # Bank filter
            driver.find_element(By.CLASS_NAME, "css-1ckc2x9").click()
            driver.find_element(By.ID, "Тинькофф").click()

            # Take info from page
            while True:

                try:
                    time.sleep(5)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    stakan = soup.find('div', class_='css-1m1f8hn')
                    buy_usdt_usd = float(stakan.text)
                    data_saver.bin_save_data(buy_usdt_usd, 'p2p_usdt_usd_buy')

                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)
            driver.close()
            rate_buy_usdt_usd()

    bin_p2p_usdt_usd = Thread(target=rate_buy_usdt_usd, args=())

    def rate_sell_usdt_usd():

        # Start driver
        driver = webdriver.Chrome(PATH_TO_WEBDRIVER)
        driver.get(URL_BINANCE_P2P_USDT_USD_SELL)

        try:
            time.sleep(5)

            # Lesson preview window with x
            driver.find_element(By.CLASS_NAME, "css-1pcqseb").click()

            # Mini pre-chat (right down)
            driver.find_element(By.CLASS_NAME, "css-1v60uza").click()

            # Fiat filter
            driver.find_element(By.CLASS_NAME, "css-1nlwvj5").click()
            driver.find_element(By.ID, "USD").click()
            time.sleep(5)

            # Merchant filter
            driver.find_element(By.CLASS_NAME, "css-5xw3l7").click()
            driver.find_element(By.CLASS_NAME, "css-l7x4y").click()
            time.sleep(5)

            # Update filter
            driver.find_element(By.CLASS_NAME, "css-qev57u").click()
            driver.find_element(By.XPATH, "//*[contains(text(), '5 с до обновления')]").click()
            time.sleep(5)

            # Bank filter
            driver.find_element(By.CLASS_NAME, "css-1ckc2x9").click()
            driver.find_element(By.ID, "Тинькофф").click()

            # Take info from page
            while True:

                try:
                    time.sleep(5)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    stakan = soup.find('div', class_='css-1m1f8hn')
                    buy_usdt_usd = float(stakan.text)
                    data_saver.bin_save_data(buy_usdt_usd, 'p2p_usdt_usd_sell')

                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)
            driver.close()
            rate_buy_usdt_usd()

    bin_p2p_usdt_usd_sell = Thread(target=rate_sell_usdt_usd, args=())

    def rate_buy_usdt_rub():

        # Start driver
        driver = webdriver.Chrome(PATH_TO_WEBDRIVER)
        driver.get(URL_BINANCE_P2P_USDT_RUB_BUY)

        try:
            time.sleep(5)

            # Lesson preview window with x
            driver.find_element(By.CLASS_NAME, "css-1pcqseb").click()
            time.sleep(5)

            # Update filter
            driver.find_element(By.CLASS_NAME, "css-qev57u").click()
            driver.find_element(By.XPATH, "//*[contains(text(), '5 с до обновления')]").click()

            # Take info from page
            while True:

                try:
                    time.sleep(5)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    stakan = soup.find('div', class_='css-1m1f8hn')
                    buy_usdt_rub = float(stakan.text)
                    data_saver.bin_save_data(buy_usdt_rub, 'p2p_usdt_rub_buy')

                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)
            driver.close()
            rate_buy_usdt_rub()

    bin_p2p_usdt_rub = Thread(target=rate_buy_usdt_rub, args=())

    def rate_sell_usdt_rub():

        # Start driver
        driver = webdriver.Chrome(PATH_TO_WEBDRIVER)
        driver.get(URL_BINANCE_P2P_USDT_RUB_SELL)

        try:
            time.sleep(5)

            # Lesson preview window with x
            driver.find_element(By.CLASS_NAME, "css-1pcqseb").click()
            time.sleep(5)

            # Update filter
            driver.find_element(By.CLASS_NAME, "css-qev57u").click()
            driver.find_element(By.XPATH, "//*[contains(text(), '5 с до обновления')]").click()

            # Take info from page
            while True:

                try:
                    time.sleep(5)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    stakan = soup.find('div', class_='css-1m1f8hn')
                    sell_usdt_rub = float(stakan.text)
                    data_saver.bin_save_data(sell_usdt_rub, 'p2p_usdt_rub_sell')

                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)
            driver.close()
            rate_sell_usdt_rub()

    bin_p2p_usdt_rub_sell = Thread(target=rate_sell_usdt_rub, args=())

    bin_p2p_usdt_rub.start()
    bin_p2p_usdt_rub_sell.start()
    bin_p2p_usdt_usd.start()
    bin_p2p_usdt_usd_sell.start()
