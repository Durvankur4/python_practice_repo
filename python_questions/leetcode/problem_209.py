# Quesiton:

# 209. Minimum Size Subarray Sum
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# # Solution:


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        min_l = float("inf")
        sum_w = 0

        for r in range(n):
            sum_w += nums[r]

            while sum_w >= target:
                min_l = min(min_l, r - l + 1)
                sum_w -= nums[l]
                l += 1

        return 0 if min_l == float("inf") else min_l


# time complexity = O(n)
# space complexity = O(n)
