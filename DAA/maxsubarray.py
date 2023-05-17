
# by divide and conquer method
def maxCrossingSum(arr, l, m, h):

	# Include elements on left of mid.
	sm = 0
	left_sum = -10000

	for i in range(m, l-1, -1):
		sm = sm + arr[i]

		if (sm > left_sum):
			left_sum = sm

	# Include elements on right of mid
	sm = 0
	right_sum = -1000
	for i in range(m, h + 1):
		sm = sm + arr[i]

		if (sm > right_sum):
			right_sum = sm

	# Return sum of elements on left and right of mid
	# returning only left_sum + right_sum will fail for [-2, 1]
	return max(left_sum + right_sum - arr[m], left_sum, right_sum)



def maxSubArraySum(arr, l, h):
	
	if (l > h):
		return -10000

	if (l == h):
		return arr[l]

	m = (l + h) // 2

	return max(maxSubArraySum(arr, l, m-1),
			maxSubArraySum(arr, m+1, h),
			maxCrossingSum(arr, l, m, h))


# take the input from the user
n = int(input("Enter the size of the array: "))
arr = []
for i in range(n):
	    arr.append(int(input("Enter the element: ")))
	    

max_sum = maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)



