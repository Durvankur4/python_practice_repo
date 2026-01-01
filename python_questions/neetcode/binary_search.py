# # Quesiton:
# Binary Search
# Solved
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Solution:


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        return self.binary_search(nums, target, l, r)

    def binary_search(self, nums, target, l, r):
        if l > r:
            return -1
        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binary_search(nums, target, mid + 1, r)
        return self.binary_search(nums, target, l, mid - 1)


# time complexity = O(n)
# space complexity = O(n)
