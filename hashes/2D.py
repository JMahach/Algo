# https://contest.yandex.ru/contest/53030/problems/D/
n, colors = map(int, input().split())
list_val = list(map(int, input().split()))
reversed_list_val = list_val[::-1]

M = 10**9 + 7
P = colors + 7

powers = [0]*(n+1)
powers[0] = 1
for i in range(1, n):
    powers[i] = (powers[i-1] * P) % M


def list_polinoms(list_val):
    m = len(list_val)
    list_hash = [list_val[0]]
    for i in range(m-1):
        list_hash.append((list_hash[i]*P + list_val[i+1]) % M)
    return list_hash


string_list_polinoms = list_polinoms(list_val)
reversed_string_list_polinoms = list_polinoms(reversed_list_val)

count = [n,]
for i in range(n//2):
    if list_val[i] == list_val[i+1]:
        if n-3-(2*i) < 0:
            if string_list_polinoms[i] == reversed_string_list_polinoms[n-2-i]:
                count.append(n-1-i)
        else:
            if string_list_polinoms[i] == \
                (reversed_string_list_polinoms[n-2-i]
                 - ((reversed_string_list_polinoms[n-3-(2*i)]
                     * powers[1+i]))) % M:
                count.append(n-1-i)

count.sort()
print(*count)
