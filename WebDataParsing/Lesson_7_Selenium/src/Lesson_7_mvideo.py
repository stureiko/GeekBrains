# ************************************************
#
# Author: Стурейко Игорь
# Project: Geekbrains.WebDataParsing
# Lesson 7 - Selenium
# Date: 2020-05-02
#
# Написать программу, которая собирает «Хиты продаж» с сайта техники mvideo и складывает данные в БД.
# Магазины можно выбрать свои.
#
# ************************************************
import json
import logging
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def get_item_info(item):
    item_info = {}
    item_info['link'] = item.get_attribute('href')
    description = json.loads(item.get_attribute('data-product-info'))
    item_info['name'] = description['productName']
    item_info['id'] = description['productId']
    item_info['price'] = description['productPriceLocal']
    logging.info(f'Обработан товар {item_info["name"]}')
    return item_info


def add_item_to_db(item_info: {}):
    """Добавляем информацию в БД"""
    client = MongoClient('localhost', 27017)
    db = client['selenium']
    # выбор коллекции документов
    coll = db['mvideo.ru']
    coll.update_one({'_id': item_info['id']}, {'$set': item_info}, upsert=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("–disable-infobars")
    options.add_argument("–enable-automation")
    options.add_argument("start-maximized")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(
        '/Users/igor/Documents/Programming/Geekbrains/WebDataParsing/Lesson_7_Selenium/src/chromedriver',
        options=options)

    try:
        logging.info('Заходим на страницу')
        driver.get("https://www.mvideo.ru/")  # заходим на страницу

        logging.info('Ждем загрузки страницы')
        hits = WebDriverWait(driver, 20).until(
            ES.presence_of_all_elements_located((By.CLASS_NAME, 'sel-hits-block')))[1]

        while True:
            logging.info('Ждем загрузки хитов')
            items = WebDriverWait(hits, 20).until(
                ES.presence_of_all_elements_located((By.CLASS_NAME, 'sel-product-tile-title')))

            logging.info('Обрабатываем результаты')
            for item in items:
                add_item_to_db(get_item_info(item))

            next_hits = WebDriverWait(hits, 30).until(
                ES.element_to_be_clickable((By.XPATH, ".//a[contains(@class, 'sel-hits-button-next')]")))
            next_hits.click()

            if 'disabled' in next_hits.get_attribute('class'):
                break
            else:
                next_hits.click()

    finally:
        driver.quit()
        logging.info('Сессия завершена')
