def binarySearch(arr, low, high):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == mid:
            return [mid] + binarySearch(arr, low, mid-1) + binarySearch(arr, mid+1, high)
        elif arr[mid] > mid:
            return binarySearch(arr, low, mid-1)
        else:
            return binarySearch(arr, mid+1, high)
    return []

# Driver program to check above functions
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
n = len(arr)
result = binarySearch(arr, 0, n-1)

if not result:
    print("No fixed points found.")
else:
    print("Fixed points found at the following indices: ", end="")
    print(*result)

