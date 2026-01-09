# # # Quesiton:
# 35. Search Insert Position
# Attempted
# Easy
# Topics
# premium lock icon
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# iven an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# # # Solution:
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:

#         l = 0
#         r = len(nums)-1

#         while l<=r:
#             mid = (l + (r - l))//2

#             if nums[mid] == target:
#                 return mid
#             elif nums[mid]>target:
#                 r = mid-1
#             else:
#                 l = mid+1
#         return l

# # # time complexity = O(n)
# # # space complexity = O(n)
