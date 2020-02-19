# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

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

def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    path = []

    cost[start] = 0
    min_cost = 0
    bs = start
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

#здесь формируются списки с путями
    for i in range(length):
        if cost[i] < float('inf'):
            path.append([i, bs])
        else:
            path.append([i, float('inf')])
        j = i
        if parent[j] >= 0:
            path[i].insert(2, j)
        while parent[j] != -1 and parent[j] != bs:
            path[i].insert(2, parent[j])
            j = parent[j]

        if (parent[j] !=  bs and parent[j] != -1):
            path[i].insert(2, parent[j])

    return cost, path


s = int(input("От какой вершины идти : "))
c, p = dijkstra(g, s)
print("Куратяайшие пути :")
print(c)
print("Списки с кратчайшими путями :")
print(*p, sep="\n")