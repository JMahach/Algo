# https://contest.yandex.ru/contest/45468/problems/40/
from collections import deque


N = int(input())
M = int(input())

lines = [() for _ in range(M+1)]
stations = [[] for _ in range(N+1)]
for i in range(1, M+1):
    lils = deque(map(int, input().split()))
    lils.popleft()
    lines[i] = tuple(lils)
for i in range(1, N+1):
    for line in lines:
        if i in line:
            stations[i].append(line)

FROM, TO = map(int, input().split())

queue = deque()
visited = {}
for line in lines:
    if FROM in line:
        visited[line] = 0
        queue.append(line)
    else:
        visited[line] = -1

while queue:
    now = queue.popleft()
    for i in now:
        for line in stations[i]:
            if visited.get(line) == -1:
                queue.append(line)
                visited[line] = visited[now] + 1

result = []
for line in stations[TO]:
    result.append(visited[line])

print(min(result))
