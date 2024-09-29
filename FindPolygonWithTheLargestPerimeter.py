# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/

# nums = [10, 10]
nums = [1, 12, 1, 2, 5, 50, 3]


def largest_perimeter(nums):
    nums.sort()
    result = -1
    sum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < sum:
            result = sum + nums[i]
        sum += nums[i]

    return result


print(largest_perimeter(nums))
