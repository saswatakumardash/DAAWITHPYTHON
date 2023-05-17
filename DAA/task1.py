def findMaximum(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    mid = n // 2
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid]
    if arr[mid] > arr[mid+1]:
        return findMaximum(arr[:mid])
    else:
        return findMaximum(arr[mid:])


arr = input("Enter the elements of the array separated by spaces: ")
arr = list(map(int, arr.split()))


max_elem = findMaximum(arr)


print("The maximum element is", max_elem)
