# https://contest.yandex.ru/contest/45469/problems/38/
from collections import deque


def create_graph(desk):
    graph = {(1, 1): set()}
    queue = deque()
    queue.append(*graph)
    holes = []
    visited = []
    while len(queue) > 0:
        point = queue.popleft()
        visited.append(point)
        y, x = point
        for i in range(y+1, N+1):  # вниз
            if desk[i][x] == 1:
                graph.setdefault(point, set()).add((i-1, x))
                if (i-1, x) not in visited:
                    queue.append((i-1, x))
                break
            elif desk[i][x] == 2:
                holes.append((i, x))
                graph.setdefault(point, set()).add((i, x))
                graph.setdefault((i, x), set())

                break
            elif i == N:
                graph.setdefault(point, set()).add((i, x))
                if (i, x) not in visited:
                    queue.append((i, x))
        for i in range(y-1, 0, -1):  # вверх
            if desk[i][x] == 1:
                graph.setdefault(point, set()).add((i+1, x))
                if (i+1, x) not in visited:
                    queue.append((i+1, x))
                break
            elif desk[i][x] == 2:
                holes.append((i, x))
                graph.setdefault(point, set()).add((i, x))
                graph.setdefault((i, x), set())
                break
            elif i == 1:
                graph.setdefault(point, set()).add((i, x))
                if (i, x) not in visited:
                    queue.append((i, x))
        for i in range(x+1, M+1):  # вправо
            if desk[y][i] == 1:
                graph.setdefault(point, set()).add((y, i-1))
                if (y, i-1) not in visited:
                    queue.append((y, i-1))
                break
            elif desk[y][i] == 2:
                holes.append((y, i))
                graph.setdefault(point, set()).add((y, i))
                graph.setdefault((y, i), set())
                break
            elif i == M:
                graph.setdefault(point, set()).add((y, i))
                if (y, i) not in visited:
                    queue.append((y, i))
        for i in range(x-1, 0, -1):  # влево
            if desk[y][i] == 1:
                graph.setdefault(point, set()).add((y, i+1))
                if (y, i+1) not in visited:
                    queue.append((y, i+1))
                break
            elif desk[y][i] == 2:
                holes.append((y, i))
                graph.setdefault(point, set()).add((y, i))
                graph.setdefault((y, i), set())
                break
            elif i == 1:
                graph.setdefault(point, set()).add((y, i))
                if (y, i) not in visited:
                    queue.append((y, i))
    return graph, holes


N, M = map(int, input().split())
desk = [[1] for _ in range(N+1)]
for i in range(1, N+1):
    desk[i].extend(list(map(int, input().split())))

graph, holes = create_graph(desk)
queue = deque()
queue.append((1, 1))
visited = {(1, 1): 0}

while len(queue) > 0:
    now = queue.popleft()
    for i in graph[now]:
        if visited.get(i, None) is None:
            queue.append(i)
            visited[i] = visited[now] + 1

res = []
for i in holes:
    res.append(visited.get(i, 10**18))
print(min(res))
