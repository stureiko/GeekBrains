"""
Представление графа
"""

from collections import namedtuple

# матрица смежности
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
]

print(*graph, sep='\n')

print('*' * 50)
# ориентированный граф
print('Ориентированный граф')
graph = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
]

print(*graph, sep='\n')

print('*' * 50)
# ориентированный взвешенный граф
print('Ориентированный взвешенный граф')
graph = [
    [0, 2, 3, 0],
    [0, 0, 2, 1],
    [0, 2, 0, 0],
    [0, 0, 0, 0],
]

print(*graph, sep='\n')

# ===========================================
# списки смежности
print('*' * 50)
print('списки смежности')
graph = []
graph.append([1, 2])
graph.append([0, 2, 3])
graph.append([0, 1])
graph.append([1])

print(*graph, sep='\n')


# ===========================================
print('*' * 50)
print('Храние в словаре')
graph_2 = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1},
    3: {1},
}

print(graph_2)

# ===========================================
print('*' * 50)
print('Храние в словаре взвешенного графа')
Vertex = namedtuple('Vertex', ['vertex', 'edge'])
graph_3 = []
graph_3.append([Vertex(1, 2), Vertex(2, 3)])
graph_3.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph_3.append([Vertex(0, 3), Vertex(1, 2)])
graph_3.append(Vertex(1, 1))

print(*graph_3, sep='\n')

for v in graph_3[1]:
    if v.vertex == 3:
        print(f'Путь из вершины 1 в 3 возможен')


# ===========================================
print('*' * 50)
print('Храние графа в классе')

class Graph:
    def __init__(self, vertex, edge):
        self.vertex = vertex
        self.edge = edge


# ===========================================
print('*' * 50)
print('Храние графа в списке ребер')

graph = [(0, 1), (0, 2), (1, 2), (2, 1), (1, 3)]
print(*graph, sep='\n')
