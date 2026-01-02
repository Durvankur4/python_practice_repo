# # Quesiton:
# 724. Find Pivot Index
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# Solution:
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        for i in range(0, len(nums)):
            rightsum = total - leftsum - nums[i]
            if rightsum == leftsum:
                return i
            leftsum += nums[i]
        return -1


# time complexity = O(n)
# space complexity = O(n)
