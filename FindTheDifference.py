# https://leetcode.com/problems/find-the-difference/description/


def find_the_difference(s, t):
    s_dict = {}
    t_dict = {}
    request_letter = ''
    for letter in s:
        s_dict[letter] = s_dict.get(letter, 0) + 1
    for letter in t:
        t_dict[letter] = t_dict.get(letter, 0) + 1
    for letter, count in t_dict.items():
        if s_dict.get(letter, 0) != count:
            request_letter += letter
            break
    return request_letter
