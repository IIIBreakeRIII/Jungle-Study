# Merge Sort Algorithm
import random

def merge_sort_gen_rnd_list(n):
    arr = [random.randint(0, 100) for _ in range(n)]
    merge_sort(arr)

def merge(arr1, arr2):
    result = []
    
    left_index = right_index = 0

    while left_index < len(arr1) and right_index < len(arr2):
        if arr1[left_index] <= arr2[right_index]:
            result.append(arr1[left_index])
            left_index += 1
        else:
            result.append(arr2[right_index])
            right_index += 1

    if left_index == len(arr1):
        result += arr2[right_index:]
    else:
        result += arr1[left_index:]

    return result

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
