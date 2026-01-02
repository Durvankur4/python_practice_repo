# Quesiton:
# 75. Sort Colors
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Solution:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0] * 3
        for num in nums:
            arr[num] += 1

        index = 0
        for i in range(3):
            while arr[i]:
                arr[i] -= 1
                nums[index] = i
                index += 1


# time complexity = O(n)
# space complexity = O(n)
