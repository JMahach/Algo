# https://leetcode.com/problems/missing-number/description/
def missing_number2(nums):
    nums.sort()
    if nums[0] != 0:
        return 0
    for i in range(1, len(nums)):
        if nums[i] - 1 != nums[i - 1]:
            return nums[i] - 1
    return nums[-1] + 1


def missing_number(nums):
    n = len(nums)
    sum_full = n * (n + 1) / 2
    sum_nums = sum(nums)
    return sum_full - sum_nums
