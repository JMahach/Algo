# https://contest.yandex.ru/contest/53032/
N = int(input())
matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]


x_cont = [False]*(N+1)
diag1 = [False]*(2*N+1)
diag2 = [False]*(2*N+1)


def rec(y, count, result):
    if count == N:
        return 1
    if y == N+1:
        return 0
    for x in range(1, N+1):
        if x_cont[x] or diag1[x+y] or diag2[x-y]:
            continue
        x_cont[x] = True
        diag1[x+y] = True
        diag2[x-y] = True
        result += rec(y+1, count+1, 0)
        x_cont[x] = False
        diag1[x+y] = False
        diag2[x-y] = False
    return result


print(rec(1, 0, 0))
