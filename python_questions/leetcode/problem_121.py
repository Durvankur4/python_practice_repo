# # Quesiton:
# 121. Best Time to Buy and Sell Stock
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxprofit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit, profit)
            else:
                left = right
            right += 1
        return maxprofit


# time complexity = O(n)
# space complexity = O(n)
