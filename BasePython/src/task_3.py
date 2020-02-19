"""
Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
import random
# Генератор случайного графа, в котором нет петель у каждой вершины есть как минимум один вход и выход.- Сильная связанность
# Граф описывается  списком смежностей
def graph_generation(number_vertices):
    graph = []
    is_in = [False] * number_vertices
    for i in range(number_vertices):
        number_edges = random.randint(1, number_vertices - 1)
        graph.append([])
        l = 0
        while l < number_edges:
            vertex = random.randint(0, number_vertices - 1)
            if vertex != i and not vertex in graph[i]:
                graph[i].append(vertex)
                is_in[vertex] = True
                l += 1
# Проверим во всех ли вершинах есть вход
    for i, data in enumerate(is_in):
        if not data:
            while not data:
                choice = random.randint(0, number_vertices - 1)
                if choice != i:
                    graph[choice].append(i)
                    is_in[i] = True
                    data = True

    return graph
# Генерация графов без проверки входов. -Возможна слабая связанность
def graph_generation_2(number_vertices):
    graph = []
    for i in range(number_vertices):
        number_edges = random.randint(1, number_vertices - 1)
        graph.append([])
        l = 0
        while l < number_edges:
            vertex = random.randint(0, number_vertices - 1)
            if vertex != i and not vertex in graph[i]:
                graph[i].append(vertex)
                l += 1

    return graph


def dfs(graph, start,visited=[]):
    if len(visited)==0:
        visited=[]
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            dfs(graph, i,visited)
    return visited


n=int(input('Введите количество вершин'))
inp=int(input("Введите точку входа"))

# Выведем граф с сильной связностью
graph=graph_generation(n)
print(graph)
print(dfs(graph,inp))

# Выведем граф без гарантии сильной связанности
graph_2=graph_generation_2(n)
print(graph_2)
print(dfs(graph_2,inp))