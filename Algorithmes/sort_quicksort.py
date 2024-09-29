def quicksort(array):
    if len(array) <= 1:
        return array
    middle_element_index = len(array) // 2
    pivot = array[middle_element_index]
    left, center, right = partition(array, pivot)
    return quicksort(left) + center + quicksort(right)


def partition(array, pivot):
    left, center, right = [], [], []
    for item in array:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        elif item == pivot:
            center.append(item)
    return left, center, right


N = int(input())
arr = list(map(int, input().split()))
result = quicksort(arr)
print(*result)
