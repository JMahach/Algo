# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/

arr = [5, 5, 4]
k = 1


def find_least_num_of_unique_ints(arr, k):
    map_arr = {}
    for i in range(len(arr)):
        map_arr[arr[i]] = map_arr.get(arr[i], 0) + 1
    sorted_list = sorted(map_arr.items(), key=lambda item: item[1])

    i = 0
    for key, value in sorted_list:
        if value <= k:
            k -= value
            i += 1
        else:
            break

    result = len(sorted_list) - i
    return result


print(find_least_num_of_unique_ints(arr, k))
