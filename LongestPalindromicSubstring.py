# https://leetcode.com/problems/longest-palindromic-substring/description/
# flake8: noqa

def longest_palindrome(s):
    M = 10**9 + 7
    P = 31
    s = "$".join(s)
    reversed_s = s[::-1]
    m = len(s)
    s_polinoms = [0] * m
    reversed_s_polinoms = [0] * m
    powers = [0] * m
    powers[0] = 1
    s_polinoms[0] = ord(s[0])
    reversed_s_polinoms[0] = ord(reversed_s[0])

    for i in range(1, m):
        powers[i] = (powers[i - 1] * P) % M
        s_polinoms[i] = (s_polinoms[i - 1] * P + ord(s[i])) % M
        reversed_s_polinoms[i] = (
            reversed_s_polinoms[i - 1] * P + ord(reversed_s[i])
        ) % M

    def check(k, *par):
        text_list_pol, reversed_text_list_pol, i, m = par
        if i - 1 - k < 0:
            h = text_list_pol[i + k]
        else:
            h = (
                text_list_pol[i + k] - text_list_pol[i - 1 - k] * powers[2 * k + 1]
            ) % M
        if m - i - 2 - k < 0:
            hr = reversed_text_list_pol[m - i - 1 + k]
        else:
            hr = (
                reversed_text_list_pol[m - i - 1 + k]
                - reversed_text_list_pol[m - i - 2 - k] * powers[2 * k + 1]
            ) % M
        return h == hr

    def right_s(left, right, *par):
        while left < right:
            k = (left + right + 1) // 2
            if check(k, *par):
                left = k
            else:
                right = k - 1
        return left

    result = []
    max_res = -1
    for i in range(len(s)):
        res = right_s(0, min(i, m - i - 1), s_polinoms, reversed_s_polinoms, i, m)
        if res > max_res or (res == max_res and s[i - res] != "$"):
            max_res = res
            result = [i, res]

    res_s = ""
    for i in range(result[1], 0, -1):
        if s[result[0] - i] == "$":
            continue
        res_s += s[result[0] - i]

    if s[result[0]] != "$":
        res_s = res_s + s[result[0]] + res_s[::-1]
    else:
        res_s = res_s + res_s[::-1]

    return res_s
