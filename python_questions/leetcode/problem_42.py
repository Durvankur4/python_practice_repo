# # Quesiton:
# 42. Trapping Rain Water
# Hard
# Topics
# premium lock icon
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Solution:
class Solution:
    def trap(self, height: List[int]) -> int:
        r, l = len(height) - 1, 0
        res = 0
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res


# time complexity = O(n)
# space complexity = O(n)
