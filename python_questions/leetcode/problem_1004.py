# # Quesiton:
# 1004. Max Consecutive Ones III
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# # Solution:
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = collections.defaultdict(int)

        total = 0
        res = 0
        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            total += 1
            while count[0] > k:  # shrink unitl valid
                count[nums[l]] -= 1
                total -= 1
                l += 1
                if not count:
                    count.pop(nums[l])
            res = max(res, total)
        return res


# time complexity = O(n)
# space complexity = O(n)
