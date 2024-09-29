# https://contest.yandex.ru/contest/53030/problems/E/
import math


M = 10**9 + 7
P = 31


def check(k, *par):
    text_list_pol, reversed_text_list_pol, i, m = par
    if i - 1 - k < 0:
        h = text_list_pol[i+k]
    else:
        h = (text_list_pol[i+k] - text_list_pol[i-1-k]*powers[2*k+1]) % M
    if m - i - 2 - k < 0:
        hr = reversed_text_list_pol[m-i-1+k]
    else:
        hr = (reversed_text_list_pol[m-i-1+k]
              - reversed_text_list_pol[m-i-2-k]*powers[2*k+1]) % M
    return h == hr


def right_s(left, right, *par):
    while left < right:
        k = (left + right + 1) // 2
        if check(k, *par):
            left = k
        else:
            right = k - 1
    return left


text = input()
reversed_text = text[::-1]

text = '$'.join(text)
m = len(text)
text_list_pol = [0]*m
reversed_text = '$'.join(reversed_text)
reversed_text_list_pol = [0]*m
powers = [0]*m

powers[0] = 1
text_list_pol[0] = ord(text[0])
reversed_text_list_pol[0] = ord(reversed_text[0])

for i in range(1, m):
    powers[i] = (powers[i-1] * P) % M
    text_list_pol[i] = (text_list_pol[i-1]*P + ord(text[i])) % M
    reversed_text_list_pol[i] = (reversed_text_list_pol[i-1]*P
                                 + ord(reversed_text[i])) % M

result = 0
for i in range(len(text)):
    res = right_s(
            0,
            min(i, m - i - 1),
            text_list_pol,
            reversed_text_list_pol, i, m)
    if text[i] == '$':
        result += math.ceil(res/2)
    else:
        result += math.floor(res/2) + 1

print(result)
