# https://leetcode.com/problems/two-sum/description/

nums = [3, 3]
target = 6


def two_sum(nums, target):
    map = {}
    n = len(nums)
    for i in range(n):
        difference = target - nums[i]
        if difference in map:
            return [map[difference], i]
        map[nums[i]] = i
    return []


print(two_sum(nums, target))
