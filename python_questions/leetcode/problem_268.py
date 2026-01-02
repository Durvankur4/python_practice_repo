# # Quesiton:
# 268. Missing Number
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


# Example 1:

# Input: nums = [3,0,1]

# Output: 2

# Explanation:

# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Solution:
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         currsum = 0
#         totalsum = n * (n+1) //2
#         for i in range(len(nums)):
#             currsum += nums[i]

#         return totalsum - currsum

# time complexity = O(n)
# space complexity = O(n)
