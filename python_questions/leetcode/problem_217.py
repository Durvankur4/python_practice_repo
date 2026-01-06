# Quesiton:
# 17. Contains Duplicate
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct

# # Solution:
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         sett = set()
#         for num in nums:
#             if num in sett:
#                 return True
#             else:
#                 sett.add(num)
#         return False

# time complexity = O(n)
# space complexity = O(n)
