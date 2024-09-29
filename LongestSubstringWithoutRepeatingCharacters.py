# https://leetcode.com/problems/longest-substring-without-repeating-characters/

s = 'abcabcbb'


def length_of_longest_substring(sanchesz):
    i = j = 0
    lenth = len(sanchesz)
    result = 0
    while i != lenth:
        if sanchesz[i] in sanchesz[j:i]:
            j += sanchesz[j:i].index(sanchesz[i]) + 1
        i += 1
        result = max(result, len(sanchesz[j:i]))
    return result


print(length_of_longest_substring(s))
