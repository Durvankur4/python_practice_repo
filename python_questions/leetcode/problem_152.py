# Quesiton:
# 152. Maximum Product Subarray
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

# Solution:


# time compleclass Solution:
def maxProduct(self, nums: List[int]) -> int:
    n = len(nums)
    ans = nums[0]
    leftp, rightp = 1, 1
    for i in range(n):
        leftp *= nums[i]
        rightp *= nums[n - 1 - i]
        ans = max(ans, leftp, rightp)
        if leftp == 0:
            leftp = 1
        if rightp == 0:
            rightp = 1
    return ans


# xity = O(n)
# space complexity = O(n)
