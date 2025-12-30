# Quesiton:

# Sort Colors
# Solved
# You are given an array nums consisting of n elements where each element is an integer representing a color:

# 0 represents red
# 1 represents white
# 2 represents blue
# Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

# You must not use any built-in sorting functions to solve this problem.
# Solution:
class Solution:
    def sort_colors(self, nums: list[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        count = [0] * 3
        for num in nums:
            count[num] += 1

        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1


# time complexity = O(n)
# space complexity = O(n)
