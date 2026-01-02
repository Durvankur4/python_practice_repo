# Quesiton:

# 169. Majority Element
# Easy
# Topics
# premium lock icon
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Solution:
# class Solution:
#     def majorityElement(self, nums: List[int]):
#         n = len(nums) // 2
#         count = {}
#         for num in nums:
#             if num in count:
#                 count[num] += 1
#             else:
#                 count[num] = 0

#         for key, value in count.items():
#             if value >= n:
#                 return key


# time complexity = O(n)
# space complexity = O(n)
