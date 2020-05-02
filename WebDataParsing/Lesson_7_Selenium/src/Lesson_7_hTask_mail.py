# ************************************************
#
# Author: Стурейко Игорь
# Project: Geekbrains.WebDataParsing
# Lesson 7 - Selenium
# Date: 2020-05-02
#
# Написать программу, которая собирает входящие письма из своего или тестового почтового ящика,
# и сложить информацию о письмах в базу данных (от кого, дата отправки, тема письма, текст письма)
#
# ************************************************

from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def get_mails():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("–disable-infobars")
    options.add_argument("–enable-automation")
    options.add_argument("–start-maximized")
    driver = webdriver.Chrome(
        '/Users/igor/Documents/Programming/Geekbrains/WebDataParsing/Lesson_7_Selenium/src/chromedriver',
        options=options)

    driver.get("https://mail.ru")  # заходим на страницу

    elem = driver.find_element_by_id('mailbox:login')
    elem.send_keys('study.ai_172@mail.ru')
    elem.send_keys(Keys.ENTER)

    elem = driver.find_element_by_id('mailbox:password')
    elem.send_keys('NewPassword172')
    elem.send_keys(Keys.ENTER)







if __name__ == '__main__':
    # get_mails()
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("–disable-infobars")
    options.add_argument("–enable-automation")
    options.add_argument("–start-maximized")
    driver = webdriver.Chrome(
        '/Users/igor/Documents/Programming/Geekbrains/WebDataParsing/Lesson_7_Selenium/src/chromedriver',
        options=options)

    driver.get("https://mail.ru")  # заходим на страницу

    elem = driver.find_element_by_id('mailbox:login')
    elem.send_keys('study.ai_172@mail.ru')
    elem.send_keys(Keys.ENTER)

    elem = driver.find_element_by_id('mailbox:password')
    elem.send_keys('NewPassword172')
    elem.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 10)

    mail = wait.until(ES.element_to_be_clickable((By.XPATH, "//a[@class='llc js-tooltip-direction_letter-bottom js-letter-list-item llc_pony-mode llc_normal']")))

    mail.click()
