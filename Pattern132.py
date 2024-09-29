# https://leetcode.com/problems/132-pattern/description/

def find_132_pattern(nums):
    stack = []
    max3 = float('-inf')
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < max3:
            return True
        while stack and stack[-1] < nums[i]:
            max3 = stack[-1]
            stack.pop()
        stack.append(nums[i])
    return False
