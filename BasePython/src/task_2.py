"""
Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
"""
from collections import deque
g=[
    [0,0,1,1,9,0,0,0],
    [0,0,8,4,0,0,5,0],
    [0,9,0,0,3,0,6,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,5,0],
    [0,0,7,0,8,1,0,0],
    [0,0,0,0,0,1,2,0]
]
def deijkstra(graph,start):
    st=start
    lengraph=len(graph)
    is_visited=[False]*lengraph
    cost=[float('inf')]*lengraph
    cost[start]=0
    min_cost=0
    parent=[-1]*lengraph
    while min_cost<float('inf'):
        is_visited[start]=True
        for i,vertex in enumerate(graph[start]):
            if vertex!=0 and not is_visited[i]:
                if cost[i]>vertex+cost[start]:
                    cost[i]=vertex+cost[start]
                    parent[i]=start

        min_cost=float('inf')
        for i in range (lengraph):
            if cost[i]<min_cost and not is_visited[i]:
                min_cost=cost[i]
                start=i
    routes=[[] for _ in range(lengraph)]

    for i,stop in enumerate(parent):
        routes[i]=deque([i])
        if stop == -1:
            continue
        while stop!=st:
            routes[i].appendleft(stop)
            j=stop
            stop=parent[j]
        else:routes[i].appendleft(st)
    return routes

print(*deijkstra(g,0),sep='\n')


