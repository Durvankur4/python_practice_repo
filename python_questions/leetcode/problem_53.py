# Quesiton:

# 53. Maximum Subarray
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Solution:


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float("-inf")
        currsum = 0

        for i in range(len(nums)):
            currsum += nums[i]
            if currsum > maxsum:
                maxsum = currsum
            if currsum < 0:
                currsum = 0

        return maxsum


# time complexity = O(n)
# space complexity = O(n)
