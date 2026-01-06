# REVSION 3/1/26
# (Do in order. Do not skip instruction lines.)

# SET 1 — PREFIX SUM FUNDAMENTALS
# Instruction: Do NOT code first. Write the prefix sum array and explain what each index represents.
# 1480 - Running Sum of 1D Array

# 724 - Find Pivot Index
# 303 - Range Sum Query - Immutable
# Goal: Prefix sums should feel obvious, not clever.

# SET 2 — PREFIX SUM + COUNTING (CRITICAL SET)
# Instruction: For each problem, write:
# (1) what the prefix sum means
# (2) what the hashmap stores
# (3) when the answer increases
# 560 - Subarray Sum Equals K
# 525 - Contiguous Array
# 930 - Binary Subarrays With Sum
# 1248 - Count Number of Nice Subarrays
# Goal: Permanently separate counting subarrays from sliding window in your brain.

# SET 3 — FIXED SLIDING WINDOW
# Instruction: Solve in one pass using a running sum.
# No maps. No extra arrays.
# 643 - Maximum Average Subarray I
# Goal: Window mechanics should be automatic.

# SET 4 — VARIABLE SLIDING WINDOW (AT MOST / MIN SIZE)
# Instruction: Before coding, state the rule for when the left pointer moves.
# 209 - Minimum Size Subarray Sum
# 904 - Fruit Into Baskets
# 1004 - Max Consecutive Ones III
# Goal: Learn when shrinking is mandatory, not optional.

# SET 5 — TWO POINTERS (OPPOSITE ENDS)
# Instruction: Explain why moving the “worse” pointer is always safe before coding.
# 11 - Container With Most Water
# 75 - Sort Colors
# Goal: Trust pointer movement logic instead of brute force.

# SET 6 — GREEDY STATE TRACKING
# Instruction: Write the state variables and what invariant they maintain.
# 121 - Best Time to Buy and Sell Stock
# 334 - Increasing Triplet Subsequence
# Goal: Understand what information is worth keeping — and what isn't.

# SET 7 — DYNAMIC PROGRAMMING (SINGLE STATE)
# Instruction: Define the recurrence in plain English before writing code.
# 53 - Maximum Subarray
# Goal: Stop thinking DP is “arrays + loops”.

# SET 8 — DUAL-STATE DP (MIND-BENDER SET)
# Instruction: Explicitly track both “best” and “worst” at every step.
# 152 - Maximum Product Subarray
# Goal: Accept that negatives flip reality.

# SET 9 — BOUNDARY / WALL LOGIC
# Instruction: Draw the left max and right max arrays or pointers on paper first.
# 42 - Trapping Rain Water
# Goal: Think in boundaries, not elements.

# SET 10 — IN-PLACE ARRAY MANIPULATION
# Instruction: Memorize the steps.
# Do NOT try to re-derive.
# 31 - Next Permutation
# Goal: Treat this like long division — procedural memory is fine.

# FINAL RULE FOR THE DAY
# If you can:
# classify the pattern in under 30 seconds
# explain the core idea without code
# The problem is locked in memory.


# answers
# 1480
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         cur_sum = 0
#         ans = [0] * len(nums)
#         for i in range(len(nums)):
#             cur_sum += nums[i]
#             ans[i] = cur_sum
#         return ans

# 725?
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         total = sum(nums)
#         leftsum = 0
#         for i in range(len(nums)):
#             rightsum = total - leftsum - nums[i]
#             if rightsum == leftsum :
#                 return i
#             leftsum += nums[i]
#         return -1

# 303
# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.ps = [0]* (len(nums)+1)
#         for i in range(1,len(nums)+1):
#             self.ps[i] = self.ps[i-1] + self.nums[i-1]

#     def sumRange(self, left: int, right: int) -> int:
#         return self.ps[right+1] - self.ps[left]


# # 560
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         total = 0
#         dict = {}
#         count = 0

#         for i in range(len(nums)):
#             total   += nums[i]
#             if total == k:
#                 count += 1
#             if (total-k) in dict:
#                 count += dict[total-k]
#             if total in dict:
#                 dict[total] +=1
#             else:
#                 dict[total] = 1
#         return count

# 525: very hard and non intutive
# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         zero, one  = 0,0
#         res = 0
#         dict = {} #count[1] - count[0] -> index i

#         for i,n in enumerate(nums):
#             if n == 0 :
#                 zero += 1
#             else:
#                 one += 1

#             if  one-zero not in dict:
#                 dict[one-zero] = i

#             # update res
#             if zero == one :
#                 res = zero + one
#             else:
#                 idx = dict[one-zero]
#                 res = max(res,i - idx)
#         return res
# 930
# 1248 both too hard for my understanding currently

# # 643
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         max_avg = 0
#         l = 0
#         curr_sum = 0

#         #to grow the window
#         for r in range(k):
#             curr_sum += nums[r]
#         max_avg = curr_sum / k

#         #slide the window
#         for r in range(k,len(nums)):
#             curr_sum = curr_sum + nums[r] - nums[l]
#             max_avg = max(max_avg,curr_sum/k)
#             l+=1

#         return max_avg

# #209
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         l= 0
#         min_len = float('inf')
#         sum = 0

#         for r in range(len(nums)):
#             sum += nums[r]

#             while sum >= target:
#                 min_len = min(min_len,r-l+1)
#                 sum -= nums[l]
#                 l+=1

#         return 0 if min_len == float('inf') else min_len

# # 904
# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         count = 0
#         dict = collections.defaultdict(int)
#         l = 0
#         max_fruits = float('-inf')

#         for r in range(len(fruits)):
#             #expand
#             f = fruits[r]
#             count += 1
#             dict[f] += 1
#             #shrink until valid
#             while len(dict)>2:
#                 l_f = fruits[l]
#                 dict[l_f] -= 1
#                 count -= 1
#                 if dict[l_f] == 0:
#                     dict.pop(l_f)
#                 l += 1

#             max_fruits = max(max_fruits ,count)
#         return max_fruits


# # 1004
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         l = 0
#         counter = 0
#         freq = {0:0,1:0}
#         max_window = float('-inf')

#         for r in range(len(nums)):
#             freq[nums[r]] += 1
#             counter += 1

#             while freq[0] > k:
#                 freq[nums[l]] -= 1
#                 counter -= 1
#                 l+= 1

#             max_window = max(max_window,counter)
#         return max_window

# #11
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         curr_cap = 0
#         n = len(height)
#         l,r = 0, n-1
#         max_cap = float('-inf')

#         while True:
#             curr_cap = min(height[l],height[r]) * (r - l)
#             max_cap = max(max_cap,curr_cap)

#             if r == l :
#                 break
#             if height[l]>height[r]:
#                 r -= 1
#             else:
#                 l+=1
#         return max_cap

# 75
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         array = [0]* 3

#         for num in nums :
#             array[num] += 1
#         idx = 0

#         for i in range(3):
#             while array[i]:
#                 nums[idx] = i
#                 array[i] -= 1
#                 idx +=1

# #121
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         cheapest = float('inf')
#         max_profit = 0
#         curr_profit= 0

#         for  r in range(len(prices)):
#             cheapest = min(cheapest,prices[r])
#             curr_profit = prices[r] - cheapest
#             max_profit = max(max_profit,curr_profit)
#         return max_profit

# 344
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         i=0
#         first = float('inf')
#         second = float('inf')
#         while i<len(nums):
#             n = nums[i]
#             if n<=first :
#                 first = n
#             elif n<=second:
#                 second = n
#             else:
#                 return True
#             i+=1
#         return False

# 53
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         curr_sum = 0
#         max_sum = nums[0]

#         for i in range(len(nums)):
#             curr_sum += nums[i]
#             max_sum = max(curr_sum,max_sum)
#             if curr_sum < 0:
#                 curr_sum = 0

#         return max_sum

# 152 very hard
# 42 hard
# 31 harddddddddgg
