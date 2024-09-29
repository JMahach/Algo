# https://contest.yandex.ru/contest/45468/problems/32/
import sys

sys.setrecursionlimit(10000000)


def dfs(graph, now, count, result):
    graph[now][1] = count
    result.append(now)
    for nieg in graph[now][0]:
        if graph[nieg][1] == 0:
            dfs(graph, nieg, count, result)


N, M = map(int, input().split())
adjacency_list = [[set(), 0] for _ in range(N+1)]
adjacency_list[0] = 0
if M != 0:
    for _ in range(1, M+1):
        V, E = map(int, input().split())
        adjacency_list[V][0].add(E)
        adjacency_list[E][0].add(V)
    count = 1
    results = []
    for i in range(1, len(adjacency_list)):
        if adjacency_list[i][1] == 0:
            result = []
            dfs(adjacency_list, i, count, result)
            results.append(result)
            count += 1
    print(count - 1)
    for r in results:
        print(len(r), ' '.join(map(str, r)), sep='\n')
else:
    print(N)
    for i in range(1, N+1):
        print(1, i, sep='\n')
