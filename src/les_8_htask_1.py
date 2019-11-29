def friends_hadshake(num: int) -> int:
    if num < 2:
        return 0
    graph = []

    for i in range(num):
        for j in range(num):
            if i != j:
                graph.append((i, j))
    return len(graph) // 2


if __name__ == '__main__':
    print(friends_hadshake(10))
