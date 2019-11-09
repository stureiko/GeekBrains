"""1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""

from collections import defaultdict


while True:
    try:
        num_facilities = int(input('Введите количество предприятий для анализа: '))
        if num_facilities < 1:
            raise ValueError('Non natural number of facilities.')
        else:
            break
    except ValueError:
        print('Вы ввели недопустимое значение. Введите натуральное число.')
        continue

res = defaultdict(list)
for i in range(1, num_facilities+1):
    facility_name = input(f'Введите название {i}-го предприятия: ')
    for period in range(1, 6):  # вносим в словарь баланс по кварталам и сразу считаем сумму по году
        if period == 5:  # если квартал == 5 - то это сумма за год
            res[facility_name].append(sum(res[facility_name]))
        else:
            while True:
                try:
                    val = float(input(f'Введите баланс за квартал - {period}: '))
                    break
                except ValueError:
                    print('Вы ввели недопустимое значение. Введите число число.')
                    continue
            res[facility_name].append(val)

# print(res)

aver_all = 0  # среднее по всем предприятиям

for name in res.keys():  # считаем среднее по всем предприятиям
    aver_all += res[name][4]
aver_all = aver_all / len(res.keys())

facility_good = []  # лучше среднего
facility_bad = []  # хуже среднего

for name in res.keys():  # пробегаем по всем предприятиям и разносим по разным спискам
    if res[name][4] > aver_all:
        facility_good.append(name)
    else:
        facility_bad.append(name)

print(f'Предприятия сработавшие лучше среднего: {facility_good}')
print(f'Предприятия сработавшие хуже среднего: {facility_bad}')
