# ************************************************
#
# Author: Стурейко Игорь
# Project: Geekbrains.WebDataParsing
# Lesson 3 - MongoDB
# Date: 2020-04-15
#
# 1) Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию,
#    записывающую собранные вакансии в созданную БД
# 2) Написать функцию, которая производит поиск и выводит на экран вакансии с
#    заработной платой больше введенной суммы
# 3*)Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта
#
# ************************************************

# ************************************************
# 1) Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию,
#    записывающую собранные вакансии в созданную БД
# ************************************************

# воспользуемся json файлом, созданным на предыдущем уроке

import json
from pymongo import MongoClient
from pprint import pprint


def add_doc_in_db(coll, file_name):
    with open(file_name, "r") as f:
        data = json.load(f)

    # Как самый простой вариант, но при повторном запуске добавим дубликаты
    # coll.insert_many(data)

    # Проверим на дубликаты и добавим только те, которых нет
    # это понадобится на 3 задании
    for doc in data:
        if coll.count_documents(doc) < 1:
            coll.insert_one(doc)


# ************************************************
# 2) Написать функцию, которая производит поиск и выводит на экран вакансии с
#    заработной платой больше введенной суммы
# ************************************************
def get_vacancies(coll, num: int)->[]:
    res = []
    count = coll.count_documents({"vacancy_money.0": {"$gt": num}})
    vacs = coll.find({'vacancy_money.0': {'$gt': num}, 'vacancy_money.2': 'руб.'})
    for vac in vacs:
        res.append(vac)
    return res

if __name__ == '__main__':

    file_name = 'vacancies_python.json'
    client = MongoClient('localhost', 27017)
    db = client['vacancies']
    # выбор коллекции документов
    coll = db['vacancies']

    # Очистить БД
    # coll.drop()

    # # Задание 1 - загрузка содержимого выборки в БД
    # # дубликаты не грузим - только уникальные записи
    add_doc_in_db(coll, file_name)
    # #
    # # # Вывести количество записей в БД
    print(f'Vacancies in db: {coll.estimated_document_count()}')
    # #
    # # # Задание 2 - поиск вакансий в БД
    vacs = get_vacancies(coll, 100000)
    for vac in vacs:
        pprint(vac)
