# ************************************************
#
# Author: Стурейко Игорь
# Project: Geekbrains.Algorithms
# Lesson 8 - Графы, хранение, поиск в ширину и глубину
# Date: 2019-11-22
#
# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
#
# ************************************************


def dijkstra(graph, start):
    """
    Алгоритм Дейкстры
    :param graph: исходный граф, представлен матрицей смежности
    :param start: начальный узел
    :return:
    """
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0
    way = {}

    while min_cost < float('inf'):
        is_visited[start] = True
        way[start] = []

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    way[start].append(i)

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    list_keys = list(way.keys())
    list_keys.sort()
    for k in list_keys:
        print(f'{k}: {way[k]}')

    return cost


if __name__ == '__main__':

    s = 0
    g = [
        [0, 0, 1, 1, 9, 0, 0, 0],
        [0, 0, 9, 4, 0, 0, 5, 0],
        [0, 9, 0, 0, 3, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 7, 0, 8, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 0],
    ]
    print(dijkstra(g, s))
