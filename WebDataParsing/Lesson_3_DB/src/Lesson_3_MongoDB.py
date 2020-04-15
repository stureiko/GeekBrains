from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('localhost', 27017)

    # БД можно выбрать и так
    db = client['test_database']

    # выбор коллекции документов
    coll = db['mycoll']

    # осуществляем добавление документа в коллекцию,
    # который содержит поля name и surname - имя и фамилия

    # doc = {"name": "Иван", "surname": "Иванов"}
    # coll.insert_one(doc)
    #
    # doc = {"name": "Василий", "surname": "Петров"}
    # coll.insert_one(doc)

    # подсчет количества людей с именем Петр
    # print(coll.count_documents({"name": "Иван"}))
    #
    # for men in coll.find():
    #     print(men)
    #
    # print('find_and_delete')
    #
    # coll.delete_many({"name": "Иван", "surname": "Иванов"})

    # for men in coll.find():
    #     print(men)
    #
    # doc = [{"name": "Иван", "surname": "Иванов"}, {"name": "Иван1", "surname": "Иванов1"}]
    # coll.insert_many(doc)
    #
    # print('* '*20)
    #
    # for men in coll.find():
    #     print(men)

    print(type(coll))

    print(db.list_collection_names())

    for col in db.list_collection_names():
        print(f'\n{col}')
        for item in db[col].find():
            print(item)
