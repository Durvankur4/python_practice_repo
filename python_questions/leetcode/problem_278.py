# # Quesiton:
# 278. First Bad Version
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# # Solution:

# # The isBadVersion API is already defined for you.
# # def isBadVersion(version: int) -> bool:

# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         l, r = 1, n

#         while l<r:
#             mid = (l+r)//2
#             if isBadVersion(mid):
#                 r = mid
#             else:
#                 l = mid + 1

#         return l
# # time complexity = O(n)
# # space complexity = O(n)
