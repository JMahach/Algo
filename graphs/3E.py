# https://contest.yandex.ru/contest/53031/problems/E/
import heapq
# import time


def dijkstra_algorithm(start, graph):
    stack = [start]
    coast_visited = [-1]*(N+1)
    coast_visited[start] = 0
    visited = [None]*(N+1)
    while stack:
        cur_node = stack.pop()
        for next in graph[cur_node]:
            next_node, next_node_cost = next
            new_cost = coast_visited[cur_node] + next_node_cost
            if coast_visited[next_node] == -1:
                stack.append(next_node)
                coast_visited[next_node] = new_cost
                visited[next_node] = cur_node
    return visited, coast_visited


def dijkstra_algorithm_fg(start, graph, swap_ya, speed_ya):
    heap = []
    heapq.heappush(heap, (0, start))

    coast_visited = [-1]*(N+1)
    coast_visited[start] = 0
    visited = [None]*(N+1)

    while heap:
        cur_time, cur_sity = heapq.heappop(heap)
        if cur_time > coast_visited[cur_sity]:
            continue
        for road in graph[cur_sity]:
            sity, road_l = road
            new_time_sity = swap_ya[sity] + (road_l/speed_ya[sity]) + cur_time
            if (coast_visited[sity] == -1
                    or new_time_sity < coast_visited[sity]):
                heapq.heappush(heap, (new_time_sity, sity))
                coast_visited[sity] = new_time_sity
                visited[sity] = cur_sity
    return visited, coast_visited


N = int(input())
swap_ya = [-1]*(N+1)
speed_ya = [-1]*(N+1)
for i in range(1, N+1):
    t, v = map(int, input().split())
    swap_ya[i], speed_ya[i] = (t, v)
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, s = map(int, input().split())
    graph[a].append((b, s))
    graph[b].append((a, s))

# start_time = time.time()

full_graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    visited, coast_visited = dijkstra_algorithm(i, graph)
    for j in range(1, len(coast_visited)):
        full_graph[i].append((j, coast_visited[j]))

# execution_time = time.time() - start_time
# print("\nВремя выполнения full_graph:", execution_time, "секунд.")
# execution_time = time.time()

visited, coast_visited = dijkstra_algorithm_fg(1, full_graph,
                                               swap_ya, speed_ya)

result = max(coast_visited)
print(result)

prev = coast_visited.index(result)
way = [prev,]
while visited[prev] is not None:
    prev = visited[prev]
    way.append(prev)
print(*way)

# execution_time = time.time() - execution_time
# print("Время выполнения way:", execution_time, "секунд.")
