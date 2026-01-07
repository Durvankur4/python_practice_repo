# # Quesiton:

# 523. Continuous Subarray Sum
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
# # Solution:

# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         freq = {0:-1}
#         prefix_sum = 0
#         for i,n in enumerate(nums):
#             prefix_sum += n
#             r = prefix_sum % k

#             if r not in freq:
#                 freq[r] = i
#             elif i - freq[r] > 1:
#                 return True
#         return False

# # time complexity = O(n)
# # space complexity = O(n)
