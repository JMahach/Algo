# https://contest.yandex.ru/contest/53033
import heapq


def dijkstra(start, graph):
    heap = []
    heapq.heappush(heap, (-float('inf'), 0, start))
    weight_visited = [0]*(N+1)
    weight_visited[start] = float('inf')

    while heap:
        cur_weight, cur_time, cur_node = heapq.heappop(heap)
        cur_weight *= -1
        if cur_weight < weight_visited[cur_node]:
            continue
        for road in graph[cur_node]:
            node, time, weight = road
            if cur_time + time > 1440:
                continue
            new_weight = min(cur_weight, weight)
            if new_weight > weight_visited[node]:
                heapq.heappush(heap, (new_weight*(-1), cur_time + time, node))
                weight_visited[node] = new_weight
    return weight_visited


N, M = map(int, input().split())
if N == 1:
    print(10**7)
else:
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, t, w = map(int, input().split())
        graph[a].append((b, t, w))
        graph[b].append((a, t, w))
    fura_weight = 3000000

    max_weigth = dijkstra(1, graph)
    if max_weigth[N] < fura_weight:
        print(0)
    else:
        result = (max_weigth[N] - fura_weight)//100
        print(str(result))
