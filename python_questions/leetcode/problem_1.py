# # Quesiton:
# 1. Two Sum
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# # Solution:
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         freq = {}
#         for i,n in enumerate(nums):
#             if target-n in freq :
#                 return [i,freq[target-n]]
#             else:
#                 freq[n] = i


# # time complexity = O(n)
# # space complexity = O(n)
