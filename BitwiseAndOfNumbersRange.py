# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/


def range_bitwise_and2(left, right):
    result = left
    for i in range(left + 1, right + 1):
        result = result & i
    return result


def range_bitwise_and(left, right):
    shift = 0
    while left != right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift
