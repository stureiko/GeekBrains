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


def get_mail_info(driver: webdriver.Chrome)->{}:
    """Разбираем информацию со страницы письма"""
    mail = {}
    wait = WebDriverWait(driver, 10)
    title = wait.until(ES.presence_of_element_located((By.XPATH,
                                               "//td[@class='readmsg__theme-box__line']")))
    mail['title'] = title.text

    letter_from = wait.until(ES.presence_of_element_located((By.XPATH,
                                                             "//div[@class='readmsg__text-container__inner-line']/a")))
    mail['from'] = letter_from.text
    letter_date = wait.until(ES.presence_of_element_located((By.XPATH,
                                                             "//span[@class='readmsg__mail-date']")))
    mail['data'] = letter_date.text
    letter_body = wait.until(ES.presence_of_element_located((By.ID,
                                                             "readmsg__body")))
    mail['body'] = letter_body.text

    if driver.current_url[-1] == '/':
        mail['id'] = driver.current_url.split('/')[-2]
    else:
        mail['id'] = driver.current_url.split('/')[-1]

    return mail


def add_mail_to_db(mail: {}):
    """Добавляем информацию в БД"""
    client = MongoClient('localhost', 27017)
    db = client['mails']
    # выбор коллекции документов
    coll = db['mail.ru']
    coll.update_one({'_id': mail['id']}, {'$set': mail}, upsert=True)


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("–disable-infobars")
    options.add_argument("–enable-automation")
    options.add_argument("–start-maximized")
    options.add_argument("--headless")
    driver = webdriver.Chrome(
        '/Users/igor/Documents/Programming/Geekbrains/WebDataParsing/Lesson_7_Selenium/src/chromedriver',
        options=options)

    try:
        driver.get("https://m.mail.ru/login")  # заходим на страницу

        # авторизуемся
        elem = driver.find_element_by_name('Login')
        elem.send_keys('study.ai_172@mail.ru')

        elem = driver.find_element_by_name('Password')
        elem.send_keys('NewPassword172')
        elem.send_keys(Keys.ENTER)

        # ждем в пределах 10 секунд пока страница прогрузится
        wait = WebDriverWait(driver, 10)

        # заходим в первое письмо
        mail = wait.until(ES.element_to_be_clickable((By.XPATH, "//td[@class='messageline__box']")))
        mail.click()

        # задаем сколько писем нужно собрать
        n = 5

        # проходим и нажимаем кнопу "Следующее" столько раз сколько нужно писем
        for i in range(n):
            # ждем пока кнопка прогрузится на странице
            next_btn = wait.until(ES.element_to_be_clickable((By.XPATH,
                                                              "//div[@class='readmsg__horizontal-block__right-block']/a")))

            # отправляем письмо на разбор параметров
            mail_cont = get_mail_info(driver)

            # добавляем информацию в БД
            add_mail_to_db(mail_cont)

            print(f'Letter {i+1}')
            # переходим к следующему письму
            next_btn.click()

    finally:
        driver.quit()
        print('Finish!')

