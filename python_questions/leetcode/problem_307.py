# # Quesiton:
# 307. Range Sum Query - Mutable
# Attempted
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, handle multiple queries of the following types:

# Update the value of an element in nums.

# # Solution:
# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums[:]
#         self.prefix_sum = [0] * len(nums)
#         summ = 0
#         for i in range(0,len(nums)):
#             summ += nums[i]
#             self.prefix_sum[i] = summ

#     def update(self, index: int, val: int) -> None:
#         self.nums[index] = val
#         summ = 0
#         for i in range(0,len(self.nums)):
#             summ += self.nums[i]
#             self.prefix_sum[i] = summ

#     def sumRange(self, left: int, right: int) -> int:
#         if left == 0:
#             return self.prefix_sum[right]
#         else:
#             return self.prefix_sum[right] - self.prefix_sum[left-1]


# # Your NumArray object will be instantiated and called as such:
# # obj = NumArray(nums)
# # obj.update(index,val)
# # param_2 = obj.sumRange(left,right)

# # time complexity = O(n)
# # space complexity = O(n)
