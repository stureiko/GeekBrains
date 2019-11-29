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

from collections import deque

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
    st = start
    cost[start] = 0
    min_cost = 0
    way = {}

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    routes = [[] for _ in range(length)]

    for i, stop in enumerate(parent):
        routes[i] = deque([i])
        if stop == -1:
            continue
        while stop != st:
            routes[i].appendleft(stop)
            j = stop
            stop = parent[j]
        else:
            routes[i].appendleft(st)

    return routes


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
    # print(dijkstra(g, s))
    node = 0
    for i in dijkstra(g, s):
        print(f'Node {node} routies: {i}')
        node += 1
