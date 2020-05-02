from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


if __name__ == '__main__':
    # driver = webdriver.Safari()
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("–disable-infobars")
    options.add_argument("–enable-automation")
    options.add_argument("–start-maximized")
    driver = webdriver.Chrome('/Users/igor/Documents/Programming/Geekbrains/WebDataParsing/Lesson_7_Selenium/src/chromedriver',
                              options=options)

    driver.get("https://geekbrains.ru/login")  # заходим на страницу

    # На ней можно выополнить проверки
    try:
        assert "Yandex" in driver.title
        print("OK")
    except AssertionError as e:
        print(f'No results "Yandex" found in {driver.current_url}')

    # Авторизуемся

    # elem = driver.find_element_by_id('user_email')
    # elem.send_keys('stureiko@mail.ru')
    #
    # elem = driver.find_element_by_id('user_password')
    # with open('GeekBrains.pass', 'r') as f:
    #     passw = f.read()
    #
    # elem.send_keys(passw)

    elem = driver.find_element_by_id('user_email')
    elem.send_keys('study.ai_172@mail.ru')

    elem = driver.find_element_by_id('user_password')
    elem.send_keys('Password172')

    elem.send_keys(Keys.ENTER)

    time.sleep(1)  # ждем пока страница окончательно прогрузится

    # ищем кнопку аватара
    profile = driver.find_element_by_class_name('avatar')

    driver.get(profile.get_attribute('href'))  # получаем с нее ссылку и переходим по ней

    # ищем кнопку редактировать профиль
    edit_profile = driver.find_element_by_class_name('text-sm')

    driver.get(edit_profile.get_attribute('href'))  # извлекаем из нее ссылку и переходим по ней

    # Множественный выбор
    gender = driver.find_element_by_name('user[gender]')  # переходим к полю
    # g_options = gender.find_elements_by_tag_name('option')  # получаем все значения
    # for g_option in g_options:  # проходим по всем значениям
    #     if g_option.text == 'Мужской':  # находим нужный
    #         g_option.click()  # кликаем по нему

    # Альтернативный способ через подключение библиотеки Select
    g_select = Select(gender)  # получаем список значений
    g_select.select_by_value('0')  # выбираем значение

    gender.submit()  # сохраняем изменения на странице

    # driver.close()  # Закроет только текущее окно
    # driver.quit()  # полностью закроет все окна, браузер и освободит ресурсы
