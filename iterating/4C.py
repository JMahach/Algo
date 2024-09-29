# https://contest.yandex.ru/contest/53032/
import time


def distribute_vertices(n, adjacency_matrix):
    max_weight = 0
    max_partition = []
    for i in range(1, 2**n):
        cur_partition = [0] * n
        cur_weight = 0

        if (i >> 0) & 1 or ((i >> max_r[1]) & 1) == ((i >> max_r[2]) & 1):
            continue

        for j in range(n):
            if (i >> j) & 1:
                cur_partition[j] = 2
            else:
                cur_partition[j] = 1

        for j in range(n):
            for k in range(j+1, n):
                if cur_partition[j] != cur_partition[k]:
                    cur_weight += adjacency_matrix[j][k]
        if cur_weight > max_weight:
            max_weight = cur_weight
            max_partition = cur_partition
    print(max_weight)
    print(' '.join(map(str, max_partition)))


n = int(input())
adjacency_matrix = []
max_r = (0,)
for _ in range(n):
    row = list(map(int, input().split()))
    if max(row) > max_r[0]:
        max_r = (max(row), row)
    adjacency_matrix.append(row)
max_r = (max_r[0], adjacency_matrix.index(max_r[1]), max_r[1].index(max_r[0]))

start = time.time()
distribute_vertices(n, adjacency_matrix)
print(f'time = {time.time() - start}')
