# # Quesiton:
# 2574. Left and Right Sum Differences
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed integer array nums of size n.

# Define two arrays leftSum and rightSum where:

# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

# # Solution:

# class Solution:
#     def leftRightDifference(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         leftSum = [0]*len(nums)
#         ans = [0]*len(nums)
#         rightSum = [0]*len(nums)
#         r_sum =0
#         l_sum =0
#         for i in range(1,n):
#             l_sum += nums[i-1]
#             leftSum[i] = l_sum

#         for i in range(n-2,-1,-1):
#             r_sum += nums[i+1]
#             rightSum[i] = r_sum

#         for i in range(n):
#             ans[i] = abs(leftSum[i] - rightSum[i])

#         return ans
# # time complexity = O(n)
# # space complexity = O(n)
