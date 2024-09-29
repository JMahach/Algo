# https://contest.yandex.ru/contest/45468/problems/36/
from collections import deque


N = int(input())
matrix = [[0] for _ in range(N+1)]
for i in range(1, N+1):
    matrix[i].extend(list(map(int, input().split())))
A, B = map(int, input().split())


queue = deque()
visited = [-1]*(N+1)
queue.append(A)
visited[A] = 0

while len(queue) > 0:
    next = queue.popleft()
    for i in range(1, N+1):
        if matrix[next][i] == 1 and visited[i] == -1:
            queue.append(i)
            visited[i] = visited[next] + 1


print(visited[B])
