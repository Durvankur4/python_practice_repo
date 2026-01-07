# # Quesiton:
# 1991. Find the Middle Index in Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

# # Solution:

# class Solution:
#     def findMiddleIndex(self, nums: List[int]) -> int:
#         l_count = 0
#         r_count = sum(nums)

#         for i in range(len(nums)):
#             r_count -= nums[i]
#             if l_count == r_count :
#                 return i
#             l_count += nums[i]
#         return -1
# # time complexity = O(n)
# # space complexity = O(n)
