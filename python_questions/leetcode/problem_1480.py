# Quesiton:
# 1480. Running Sum of 1d Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

Solution:
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        counter = 0
        ans = []
        for i in nums:
            counter += i
            ans.append(counter)
        return ans

# time complexity = O(n)
# space complexity = O(n)
