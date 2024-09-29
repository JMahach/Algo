# https://contest.yandex.ru/contest/45468/problems/34/
import sys

sys.setrecursionlimit(10000000)


def dfs(graph, now, res, prev=0):
    graph[now][1] = 1
    for nieg in graph[now][0]:
        if graph[nieg][1] == 0:
            if dfs(graph, nieg, res, now) == -1:
                return -1
        elif graph[nieg][1] == 1 and nieg != prev and now != nieg:
            return -1
    graph[now][1] = 2
    res.append(now)


N, M = map(int, input().split())
adjacency_list = [[set(), 0] for _ in range(N+1)]
for _ in range(1, M+1):
    V, E = map(int, input().split())
    adjacency_list[V][0].add(E)

res = []
for i in range(1, len(adjacency_list)):
    if adjacency_list[i][1] == 0:
        if dfs(adjacency_list, i, res) == -1:
            res = [-1]
            break
res.reverse()
print(*res)
