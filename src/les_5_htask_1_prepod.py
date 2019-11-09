"""1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""

from collections import namedtuple

QUARTERS = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input('Введите количество предприятий: '))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input('Введите название предприятия: ')

    for j in range(QUARTERS):
        quarters.append(int(input(f'Прибыль за {j + 1}-й квартал: ')))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)
    all_companies.add(comp)
    total_profit += profit

average = total_profit / num

print(f'Средняя прибыль составила {average}')

print(']предприятия с прибылью выше среднего:')
for comp in all_companies:
    if comp.profit > average:
        print(comp.name)

print(']предприятия с прибылью ниже среднего:')
for comp in all_companies:
    if comp.profit < average:
        print(comp.name)
