# https://contest.yandex.ru/contest/45468/problems/38/
from collections import deque


def create_graph(N, M):
    graph = {}
    directions = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                  (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            v = (i, j)
            relateds = []
            for direction in directions:
                x = v[0] + direction[0]
                y = v[1] + direction[1]
                if 1 <= x <= N and 1 <= y <= M:
                    relateds.append((x, y))
            graph[v] = relateds
    return graph


N, M, S, T, Q = map(int, input().split())
graph = create_graph(N, M)
queue = deque()
queue.append((S, T))
blohs = []
for _ in range(Q):
    blohs.append(tuple(map(int, input().split())))
visited = {}
visited[(S, T)] = 0

while len(queue) > 0:
    now = queue.popleft()
    for i in graph[now]:
        if visited.get(i, None) is None:
            queue.append(i)
            visited[i] = visited[now] + 1

result = 0
for bloha in blohs:
    if visited.get(bloha) is not None:
        result += visited[bloha]
    else:
        result = -1
        break
print(result)
