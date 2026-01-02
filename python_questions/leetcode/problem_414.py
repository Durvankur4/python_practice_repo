# Quesiton:
# 414. Third Maximum Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
# Solution:
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        if len(unique) < 3:
            return unique[-1]
        return unique[-3]


# time complexity = O(n)
# space complexity = O(n)
