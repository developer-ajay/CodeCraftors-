
def bSearch(num,target):
    low , high = 0 , len(num) - 1
    
    while low <= high:
        mid = (low + high) //2
        if num[mid] == target:
            return mid
        elif num[mid] < target:
            low = mid +1
        elif num[mid] > target:
            high = mid -1 
    
    return -1

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  

    mid = (low + high) // 2  

    if arr[mid] == target:
        return mid  
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)  
    else:
        return binary_search_recursive(arr, target, low, mid - 1) 



num = [3,7,8,14,17,21,32,39,45,51,54,59,63,72,85]
result = bSearch(num,39)
if result == -1:
    print("Target not found")
else:
    print(f"Target found at index: {result}")
    
resultr = binary_search_recursive(num,39,0,len(num)-1)
if result == -1:
    print("Target not found")
else:
    print(f"Target found at index: {result}")
