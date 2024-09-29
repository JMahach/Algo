def merge_sort(array):
    if len(array) <= 1:
        return array
    left = merge_sort(array[0:len(array)//2])
    right = merge_sort(array[len(array)//2:len(array)])
    return merge(left, right)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    return result + left[left_idx:] + right[right_idx:]


test_array = [5, 4, 9, 10, 8, 3, 11, 1, 7, 6, 2]
print(merge_sort(test_array))
