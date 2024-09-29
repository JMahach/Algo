# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
# flake8: noqa
import heapq


def findCheapestPrice2(n, flights, src, dst, k):
    graph = {}
    for flight in flights:
        graph[flight[0]] = graph.get(flight[0], [])
        graph[flight[0]].append((flight[1], flight[2]))

    heap = [(0, 0, src)]  # price,stops,city
    visited = {}

    while heap:
        price, stops, city = heapq.heappop(heap)

        if stops > k + 1:
            continue

        if city == dst:
            return price

        if city in visited and visited[city] == stops:
            continue

        visited[city] = stops

        for nei, p in graph[city]:
            if nei not in visited or visited[nei] > stops:
                heapq.heappush(heap, (price + p, stops + 1, nei))

    return -1


def findCheapestPrice(n, flights, src, dst, k):
    graph = {}
    for flight in flights:
        graph[flight[0]] = graph.get(flight[0], [])
        graph[flight[0]].append((flight[1], flight[2]))

    import heapq

    heap = []
    heapq.heappush(heap, (0, 0, src))
    visited = {}
    while heap:
        cur_cost, cur_k, cur_node = heapq.heappop(heap)

        if cur_k > k + 1:
            continue

        if cur_node == dst:
            return cur_cost

        if cur_node in visited and visited[cur_node] == cur_k:
            continue

        visited[cur_node] = cur_k

        for next_node, next_cost in graph.get(cur_node, []):
            heapq.heappush(heap, (next_cost + cur_cost, cur_k + 1, next_node))

    return -1


print(
    findCheapestPrice(
        n=13,
        flights=[
            [11, 12, 74],
            [1, 8, 91],
            [4, 6, 13],
            [7, 6, 39],
            [5, 12, 8],
            [0, 12, 54],
            [8, 4, 32],
            [0, 11, 4],
            [4, 0, 91],
            [11, 7, 64],
            [6, 3, 88],
            [8, 5, 80],
            [11, 10, 91],
            [10, 0, 60],
            [8, 7, 92],
            [12, 6, 78],
            [6, 2, 8],
            [4, 3, 54],
            [3, 11, 76],
            [3, 12, 23],
            [11, 6, 79],
            [6, 12, 36],
            [2, 11, 100],
            [2, 5, 49],
            [7, 0, 17],
            [5, 8, 95],
            [3, 9, 98],
            [8, 10, 61],
            [2, 12, 38],
            [5, 7, 58],
            [9, 4, 37],
            [8, 6, 79],
            [9, 0, 1],
            [2, 3, 12],
            [7, 10, 7],
            [12, 10, 52],
            [7, 2, 68],
            [12, 2, 100],
            [6, 9, 53],
            [7, 4, 90],
            [0, 5, 43],
            [11, 2, 52],
            [11, 8, 50],
            [12, 4, 38],
            [7, 9, 94],
            [2, 7, 38],
            [3, 7, 88],
            [9, 12, 20],
            [12, 0, 26],
            [10, 5, 38],
            [12, 8, 50],
            [0, 2, 77],
            [11, 0, 13],
            [9, 10, 76],
            [2, 6, 67],
            [5, 6, 34],
            [9, 7, 62],
            [5, 3, 67],
        ],
        src=10,
        dst=1,
        k=10,
    )
)
