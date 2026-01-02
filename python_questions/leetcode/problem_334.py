# # Quesiton:
# 334. Increasing Triplet Subsequence
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# Solution:
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")

        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False


# time complexity = O(n)
# space complexity = O(n)
