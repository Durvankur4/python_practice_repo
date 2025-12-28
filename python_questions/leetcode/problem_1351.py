# Quesiton:

# 1351. Count Negative Numbers in a Sorted Matrix
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a m x n matrix grid which is sorted in non-increasing order both
# row-wise and column-wise, return the number of negative numbers in grid.
# Solution:
class Solution:
    def count_negatives(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0
        row_index = m - 1
        col_index = 0

        while row_index >= 0 and col_index < n:
            if grid[row_index][col_index] < 0:
                count += n - col_index
                row_index -= 1
            else:
                col_index += 1

        return count


# time complexity = O(n)
# space complexity = O(n)
