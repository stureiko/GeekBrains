# ************************************************
#
# Author: Стурейко Игорь
# Project: Geekbrains.Algorithms
# Lesson 9 - Деревья, Хеш функции
# Date: 2019-11-29
#
# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
#
# ************************************************
import hashlib


if __name__ == '__main__':
    # s_1 = input('Введите строку: ')
    s_1 = 'hello'

# Реализация через массив
    pods = []
    for i in range(1, len(s_1)):
        for j in range(len(s_1)):
            sub = s_1[j:j+i]
            if sub not in pods:
                pods.append(sub)

# реализация через массив хешей
    pod2 = []
    for i in range(1, len(s_1)):
        for j in range(len(s_1)):
            sub = hashlib.sha1(s_1[j:j+i].encode('utf-8')).hexdigest()
            if sub not in pod2:
                pod2.append(sub)

# вывести результаты
    print(len(pods))
    print('*' * 50)
    # print(*pods, sep='\n')

    print(len(pod2))
