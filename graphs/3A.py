# https://contest.yandex.ru/contest/53031/problems/A/
import heapq

N, S, F = map(int, input().split())
matrix = [[-1] for _ in range(N+1)]
for i in range(1, N+1):
    row = list(map(int, input().split()))
    matrix[i].extend(row)


def dijkstra_algorithm(start, graph):
    heap = []
    heapq.heappush(heap, (0, start))

    coast_visited = {start: 0}
    visited = {start: None}

    while heap:
        cur_cost, cur_node = heapq.heappop(heap)
        if coast_visited[cur_node] < cur_cost:
            continue
        for node, cost in enumerate(matrix[cur_node]):
            if cost > 0:
                new_cost = coast_visited[cur_node] + cost
                if node not in coast_visited or new_cost < coast_visited[node]:
                    heapq.heappush(heap, (new_cost, node))
                    coast_visited[node] = new_cost
                    visited[node] = cur_node
    return visited, coast_visited


visited, coast_visited = dijkstra_algorithm(S, matrix)
print(coast_visited.setdefault(F, -1))
