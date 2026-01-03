# # Quesiton:
# 643. Maximum Average Subarray I
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Solution:
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        n = len(nums)

        for i in range(k):
            curr_sum += nums[i]

        max_sum = curr_sum

        for i in range(k, n):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k


# time complexity = O(n)
# space complexity = O(n)
