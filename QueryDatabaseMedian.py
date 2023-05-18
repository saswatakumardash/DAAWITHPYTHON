# AIM:-
# To find the median of the set of 2n values using at most O(log n) queries, we can utilize a modified version of the binary search algorithm. The basic idea is to repeatedly query the databases with a value k that partitions the values into two equal-sized groups, narrowing down the range in which the median resides.
#PROGRAM:-
def query(database, k):
    # Placeholder function for querying the database
    # Replace this with the actual implementation for querying your databases
    return database[k - 1]  # Assuming 1-based indexing for the values

def find_median(database1, database2, n):
    left = 1  # Smallest possible value in the range
    right = n  # Largest possible value in the range

    while left < right:
        mid = (left + right) // 2  # Middle value in the range

        # Query both databases with the middle value
        k1 = query(database1, mid)
        k2 = query(database2, mid)

        if k1 <= k2:
            left = mid + 1
        else:
            right = mid

    return left  # The nth smallest value is the median

# Example usage:
database1 = input("Enter values for database1 (space-separated): ").split()
database1 = list(map(int, database1))
database2 = input("Enter values for database2 (space-separated): ").split()
database2 = list(map(int, database2))
n = len(database1)

median = find_median(database1, database2, n)
print("Median:", median)
