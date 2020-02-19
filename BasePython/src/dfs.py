# ************************************************
#
# Author: Стурейко Игорь
# Project: Geekbrains.Algorithms
# Lesson 8 - Графы, хранение, поиск в ширину и глубину
# Date: 2019-11-22
#
# Задание 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
#
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин
#
# ************************************************

import random


def gen_graph(num: int) -> dict:
    """
    Генератор случайного графа
    :param num: количество вершин графа
    :return: граф в виде словаря, ключ - вершина, значение - список смежности
    """
    g = {}
    for i in range(0, num + 1):  # для каждой вершины создать список смежности
        list = []
        for j in range(random.randint(0, num)):  # количетво связей для каждой вершины случайно
            s = random.randint(0, num)  # формируем случайную связь
            if s != i and str(s) not in list:  # в графе не должно быть петель
                list.append(str(s))
        g[str(i)] = list  # добавляем в словарь
    return g


def print_graph(graph: dict):
    """
    "Удобная" печать графа
    :param g: граф в виде словаря
    """
    for item in graph.keys():
        print(f'{item}: {graph[item]}')


def dfs(graph, node, con_component):
    """
    Поиск в глубину - рекурсивная реализация
    :param graph: граф в виде словаря
    :param node: узел откуда производится поиск
    :return: con_component - компонента связности - список посещенных вершин
    """
    if node not in con_component:
        con_component.append(node)
        for n in graph[node]:
            dfs(graph, n, con_component)
    return con_component


if __name__ == '__main__':
    g = gen_graph(10)
    print_graph(g)
    print('*' * 30)

    for item in g.keys():
        con_component = dfs(g, item, [])
        print(f'for node \'{item}\': {con_component}')
