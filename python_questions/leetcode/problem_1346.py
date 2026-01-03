# Quesiton:

# 1346. Check If N and Its Double Exist
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
# Solution:


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for i in arr:
            if i * 2 in seen or (i % 2 == 0 and i / 2 in seen):
                return True
            seen.add(i)
        return False


# time complexity = O(n)
# space complexity = O(n)
