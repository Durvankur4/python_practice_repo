# # Quesiton:
# nsertion Sort is a simple sorting algorithm that builds the sorted list one element at a time, from left to right. It works by repeatedly taking an element from the unsorted portion and inserting it into its correct position in the sorted portion of the list.

# Objective:

# Given a list of key-value pairs, sort the list by key using Insertion Sort. Return a list of lists showing the state of the array after each insertion. If two key-value pairs have the same key, maintain their relative order in the sorted list.

# Solution:

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def insertion_sort(self, pairs: list[Pair]) -> list[list[Pair]]:
        lenth = len(pairs)
        result = []
        for i in range(lenth):
            j = i
            while j > 0 and pairs[j - 1].key > pairs[j].key:
                pairs[j - 1], pairs[j] = pairs[j], pairs[j - 1]
                j -= 1
            result.append(pairs[:])
        return result


# time complexity = O(n)
# space complexity = O(n)
