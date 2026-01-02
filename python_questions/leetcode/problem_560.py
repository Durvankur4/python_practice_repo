# Quesiton:
# 560. Subarray Sum Equals K
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Solution:


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        counter = 0
        dict = {}

        for i in range(len(nums)):
            total += nums[i]
            if total == k:
                counter += 1
            if (total - k) in dict:
                counter += dict[total - k]
            if total in dict:
                dict[total] += 1
            else:
                dict[total] = 1
        return counter


# time complexity = O(n)
# space complexity = O(n)
