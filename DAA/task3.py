def local_minima(n, grid):
   
    return find_local_minima(grid, 0, n - 1, 0, n - 1, n)


def find_local_minima(grid, row_start, row_end, col_start, col_end, n):
    mid_row = (row_start + row_end) // 2
    mid_col = (col_start + col_end) // 2
    min_val = min(grid[mid_row][col_start:col_end + 1])
    j = grid[mid_row].index(min_val, col_start, col_end + 1)

    if (mid_row == 0 or grid[mid_row - 1][j] > min_val) and (mid_row == n - 1 or grid[mid_row + 1][j] > min_val) and \
            (j == 0 or grid[mid_row][j - 1] > min_val) and (j == n - 1 or grid[mid_row][j + 1] > min_val):
        return (mid_row, j)

    if mid_row > 0 and grid[mid_row - 1][j] < min_val:
        return find_local_minima(grid, row_start, mid_row - 1, col_start, col_end, n)

    if mid_row < n - 1 and grid[mid_row + 1][j] < min_val:
        return find_local_minima(grid, mid_row + 1, row_end, col_start, col_end, n)

    if j > 0 and grid[mid_row][j - 1] < min_val:
        return find_local_minima(grid, row_start, row_end, col_start, j - 1, n)

    if j < n - 1 and grid[mid_row][j + 1] < min_val:
        return find_local_minima(grid, row_start, row_end, j + 1, col_end, n)

    return None


n = int(input("Enter the size of the grid (n x n): "))
grid = []
elements = set() 
for i in range(n):
    row = list(map(int, input(f"Enter the {n} elements in row {i+1}, separated by spaces: ").split()))
    grid.append(row)
    elements.update(row) 


local_min = local_minima(n, grid)


print(f"The local minimum in the grid is at index ({local_min[0]}, {local_min[1]})")
print(f"The distinct elements in the grid are: {sorted(elements)}")
