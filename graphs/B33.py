# https://contest.yandex.ru/contest/45468/problems/33/
def dfs(graph, now, visited, color):
    visited[now] = True
    graph[now][1] = 3 - color

    for nieg in graph[now][0]:
        if graph[nieg][1] == 3 - color:
            return 'NO'
        if not visited[nieg]:
            dfs(graph, nieg, visited, 3 - color)


N, M = map(int, input().split())
adjacency_list = [[set(), 0] for _ in range(N+1)]
if M != 0:
    for _ in range(1, M+1):
        V, E = map(int, input().split())
        adjacency_list[V][0].add(E)
        adjacency_list[E][0].add(V)
    visited = [False]*(N+1)

    se = set()
    for i in range(1, len(adjacency_list)):
        if adjacency_list[i][1] == 0:
            res = dfs(adjacency_list, i, visited, 1)
            se.add('YES' if res is None else res)
    print('NO' if 'NO' in se else 'YES')

else:
    print('YES')
