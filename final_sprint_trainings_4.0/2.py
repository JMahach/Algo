# https://contest.yandex.ru/contest/53033
M = 10**9 + 7
P = 31
m = int(input())
string = input()
reversed_string = string[::-1]

powers = [0]*m
string_list_hashs = [0]*m
reversed_string_list_hashs = [0]*m

powers[0] = 1
string_list_hashs[0] = ord(string[0])
reversed_string_list_hashs[0] = ord(reversed_string[0])

for i in range(1, m):
    powers[i] = (powers[i-1] * P) % M
    string_list_hashs[i] = (string_list_hashs[i-1]*P + ord(string[i])) % M
    reversed_string_list_hashs[i] = (reversed_string_list_hashs[i-1]*P
                                     + ord(reversed_string[i])) % M


def check(k, m, i):
    h = string_list_hashs[k]
    if i == m-1:
        hr = reversed_string_list_hashs[m-1-i+k]
    else:
        hr = (reversed_string_list_hashs[m-1-i+k]
              - reversed_string_list_hashs[m-2-i]*powers[k+1]) % M
    return h == hr


def right_s(left, right, m, i):
    while left <= right:
        k = (left + right + 1) // 2
        if check(k, m, i):
            left = k + 1
        else:
            right = k - 1
    return left


results = []
for i in range(m):
    res = right_s(0, i, m, i)
    results.append(res)
print(*results)
