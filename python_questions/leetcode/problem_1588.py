# # Quesiton:

# 1588. Sum of All Odd Length Subarrays
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

# A subarray is a contiguous subsequence of the array.
# # Solution:

# class Solution:
#     def sumOddLengthSubarrays(self, arr: List[int]) -> int:
#         arr_l = len(arr)
#         n = -(-arr_l//2)
#         odd_idx = []
#         total = 0
#         for x in range(1,arr_l+1,2):
#             odd_idx.append(x)

#         for i in range(len(odd_idx)):
#             wind_size = odd_idx[i]
#             l,summ = 0,0

#             for r in range(len(arr)):
#                 summ += arr[r]
#                 while r-l+1 > wind_size:
#                     summ -= arr[l]
#                     l+=1
#                 if r-l+1 == wind_size:
#                     total += summ

#         return total
# # time complexity = O(n)
# # space complexity = O(n)
