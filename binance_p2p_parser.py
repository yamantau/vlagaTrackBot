p2p_usdt_usd = -1
p2p_usdt_rub = -1

URL_BINANCE_P2P_USDT_USD = "https://p2p.binance.com/ru/trade/Tinkoff/USDT?fiat=USD"
URL_BINANCE_P2P_USDT_RUB = "https://p2p.binance.com/ru/trade/Tinkoff/USDT?fiat=RUB"
PATH_TO_WEBDRIVER = 'D:\proger\webdriver\chromedriver.exe'

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from threading import Thread


def get_p2p_usdt_usd():
    #start driver
    driver = webdriver.Chrome(PATH_TO_WEBDRIVER)
    driver.get(URL_BINANCE_P2P_USDT_USD)

    #find and click on buttoms
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "css-1pcqseb").click()
    driver.find_element(By.CLASS_NAME, "css-hut8d0").click()
    driver.find_element(By.CLASS_NAME, "css-1iztezc").click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "css-qev57u").click()
    driver.find_element(By.XPATH, "//*[contains(text(), '5 с до обновления')]").click()

    #search stakan on page
    while True:
        try:
            time.sleep(5)
            full_page = driver.page_source
            soup = BeautifulSoup(full_page, 'html.parser')
            stakan = soup.find('div', class_='css-1m1f8hn')
            global p2p_usdt_usd
            p2p_usdt_usd = float(stakan.text)
        except Exception as e:
            print(e)


bin_p2p_usdt_usd = Thread(target=get_p2p_usdt_usd, args=())


def get_p2p_usdt_rub():
    #start driver
    driver = webdriver.Chrome(PATH_TO_WEBDRIVER)
    driver.get(URL_BINANCE_P2P_USDT_RUB)

    #find and click on buttoms
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "css-1pcqseb").click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "css-qev57u").click()
    driver.find_element(By.XPATH, "//*[contains(text(), '5 с до обновления')]").click()

    #search stakan on page
    while True:
        try:
            time.sleep(5)
            full_page = driver.page_source
            soup = BeautifulSoup(full_page, 'html.parser')
            stakan = soup.find('div', class_='css-1m1f8hn')
            global p2p_usdt_rub
            p2p_usdt_rub = float(stakan.text)
        except Exception as e:
            print(e)

bin_p2p_usdt_rub = Thread(target=get_p2p_usdt_rub, args=())
