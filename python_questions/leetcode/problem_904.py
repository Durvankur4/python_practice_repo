# # Quesiton:
# 904. Fruit Into Baskets
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# Solution:
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        import collections

        count = collections.defaultdict(int)

        l = 0
        total = 0
        res = 0

        for r in range(len(fruits)):
            f = fruits[r]
            count[f] += 1
            total += 1
            while len(count) > 2:
                count[fruits[l]] -= 1
                total -= 1
                if not count[fruits[l]]:
                    count.pop(fruits[l])
                l += 1
            res = max(res, total)
        return res


# time complexity = O(n)
# space complexity = O(n)
