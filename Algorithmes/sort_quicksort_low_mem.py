import sys
import random


def partition(arr, start, end, x):
    left, mid, rigth = start, start, start
    for i in range(start, end):
        if arr[i] < x:
            arr[rigth], arr[mid], arr[left] = arr[mid], arr[left], arr[rigth]
            left, mid, rigth = left + 1, mid + 1, rigth + 1
        elif arr[i] == x:
            arr[rigth], arr[mid] = arr[mid], arr[rigth]
            mid, rigth = mid + 1, rigth + 1
        else:
            rigth += 1
    return left


def quick_sort(arr, low, high):
    if low < high:
        pivot = random.choice(arr[low:high])
        pi = partition(arr, low, high, pivot)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)


N = int(input())

if N != 0:
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    if len(set(arr)) != 1:
        quick_sort(arr, 0, N)
    print(*arr)
else:
    print('')
