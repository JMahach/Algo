import heapq


graph = {
    1: [(2, 15), (3, 10)],
    2: [(1, 15), (4, 7)],
    3: [(1, 10), (4, 20)],
    4: [(3, 20), (2, 7)],
}


def dijkstra_algorithm(start, goal, graph):
    heap = []
    heapq.heappush(heap, (0, start))
    coast_visited = {start: 0}
    visited = {start: None}
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)
        if cur_cost > coast_visited[cur_node]:
            continue
        # if cur_node == goal:
        #     break
        next_nodes = graph[cur_node]
        for next in next_nodes:
            next_node, next_node_cost = next
            new_cost = coast_visited[cur_node] + next_node_cost
            if (next_node not in coast_visited
                    or new_cost < coast_visited[next_node]):
                heapq.heappush(heap, (new_cost, next_node))
                coast_visited[next_node] = new_cost
                visited[next_node] = cur_node
    return visited, coast_visited


visited, coast_visited = dijkstra_algorithm(1, 4, graph)

print(coast_visited[4])
