# https://contest.yandex.ru/contest/53033
import time


def search(x):
    result = []
    i, j = 1, 1
    while len(result) < x:
        ir = i**2
        jr = j**3
        if ir == jr:
            result.append(ir)
            i += 1
            j += 1
        elif ir < jr:
            result.append(ir)
            i += 1
        else:
            result.append(jr)
            j += 1
    return result[x-1]


x = int(input())
start = time.time()
result = search(x)
print(result, f'\ntime = {time.time() - start}', sep='\n')
