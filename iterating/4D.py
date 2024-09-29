# https://contest.yandex.ru/contest/53032/
def shortest_way(dist, V, rem, min_r):
    if False not in used:
        used[0] = min(dist+matrix[V][1], used[0])
        return
    if dist+(rem*min_r) >= used[0]:
        return
    for i in range(1, N+1):
        if used[i] or dist+matrix[V][i] >= used[0] or matrix[V][i] == 0:
            continue
        used[i] = True
        shortest_way(dist+matrix[V][i], i, rem-1, min_r)
        used[i] = False


N = int(input())
if N == 0:
    print(-1)
else:
    matrix = [[0] for _ in range(N+1)]
    min_r = float('inf')
    for i in range(1, N+1):
        v = list(map(int, input().split()))
        for el in v:
            if el != 0 and el < min_r:
                min_r = el
        matrix[i].extend(v)
    used = [False]*(N+1)
    used[1] = True
    used[0] = float('inf')
    shortest_way(0, 1, N, min_r)
    if used[0] == float('inf'):
        print(-1)
    else:
        print(used[0])
