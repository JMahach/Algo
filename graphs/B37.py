# https://contest.yandex.ru/contest/45468/problems/37/
from collections import deque


N = int(input())
matrix = [[0] for _ in range(N+1)]
for i in range(1, N+1):
    matrix[i].extend(list(map(int, input().split())))
A, B = map(int, input().split())


queue = deque()
visited = [-1]*(N+1)
prev = [-1]*(N+1)

queue.append(A)
visited[A] = 0

while len(queue) > 0:
    now = queue.popleft()
    for i in range(1, N+1):
        if matrix[now][i] == 1 and visited[i] == -1:
            queue.append(i)
            visited[i] = visited[now] + 1
            prev[i] = now


print(visited[B])
if visited[B] >= 1:
    result = [B,]
    i = 0
    while prev[result[i]] >= 0:
        result.append(prev[result[i]])
        i += 1
    result.reverse()
    print(*result)
