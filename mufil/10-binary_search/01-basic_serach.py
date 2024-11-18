arr = [3,7,8,14,17,21,32,39,45,51,54,59,63,72,85]

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search(arr, 85))
print(binary_search(arr, 89))