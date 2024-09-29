# https://contest.yandex.ru/contest/45468/problems/31/
def dfs(graph, visited, now, result):
    visited[now] = True
    result.append(now)
    for nieg in graph[now]:
        if not visited[nieg]:
            dfs(graph, visited, nieg, result)


N, M = map(int, input().split())
adjacency_list = {}
if M != 0:
    V, E = map(int, input().split())
    now = V
    adjacency_list.setdefault(V, []).append(E)
    adjacency_list.setdefault(E, []).append(V)
    for _ in range(2, M+1):
        V, E = map(int, input().split())
        adjacency_list.setdefault(V, []).append(E)
        adjacency_list.setdefault(E, []).append(V)

    result = []
    visited = [False]*(N+1)
    dfs(adjacency_list, visited, now, result)
    print(len(result))
    print(*sorted(result))
else:
    print(*(1, 1), sep='\n')
