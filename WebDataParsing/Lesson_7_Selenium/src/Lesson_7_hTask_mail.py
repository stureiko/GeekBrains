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
import time


def get_mail_info(driver: webdriver.Chrome):
    wait = WebDriverWait(driver, 10)
    title = wait.until(ES.presence_of_element_located((By.XPATH,
                                                       "//h2[@class='thread__subject thread__subject_pony-mode']")))
    print(f'Title: {title.text}')
    letter_from = wait.until(ES.presence_of_element_located((By.XPATH,
                                                             "//div[@class='letter__author']/span")))
    print(f'From: {letter_from.text}')
    letter_date = wait.until(ES.presence_of_element_located((By.XPATH,
                                                             "//div[@class='letter__author']/div[@class='letter__date']")))
    print(f'Date: {letter_date.text}')
    letter_body = wait.until(ES.presence_of_element_located((By.XPATH,
                                                             "//table[4]//tbody[1]//tr[2]//td[1]//table[1]//tbody[1]")))
    print(f'Body: {letter_body.text}')

    return 'OK'


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("–disable-infobars")
    options.add_argument("–enable-automation")
    options.add_argument("–start-maximized")
    driver = webdriver.Chrome(
        '/Users/igor/Documents/Programming/Geekbrains/WebDataParsing/Lesson_7_Selenium/src/chromedriver',
        options=options)

    try:
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

        get_mail_info(driver)

        # wait = WebDriverWait(driver, 10)
        # title = wait.until(ES.presence_of_element_located((By.XPATH,
        #                                              "//h2[@class='thread__subject thread__subject_pony-mode']")))
        # print(f'Title: {title.text}')
        # letter_from = wait.until(ES.presence_of_element_located((By.XPATH,
        #                                              "//div[@class='letter__author']/span")))
        # print(f'From: {letter_from.text}')
        # letter_date = wait.until(ES.presence_of_element_located((By.XPATH,
        #                                             "//div[@class='letter__author']/div[@class='letter__date']")))
        # print(f'Date: {letter_date.text}')
        # letter_body = wait.until(ES.presence_of_element_located((By.XPATH,
        #                                                 "//table[4]//tbody[1]//tr[2]//td[1]//table[1]//tbody[1]")))
        # print(f'Body: {letter_body.text}')

    finally:
        driver.quit()

