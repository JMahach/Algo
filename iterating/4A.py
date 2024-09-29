# https://contest.yandex.ru/contest/53032/
def generate_permutations(n, perm, used):
    if len(perm) == n:
        print(''.join(map(str, perm)))
        return

    for i in range(1, n+1):
        if not used[i]:
            perm.append(i)
            used[i] = True
            generate_permutations(n, perm, used)
            used[i] = False
            perm.pop()


N = int(input())
used = [False] * (N+1)
generate_permutations(N, [], used)
