# Quesiton:

# Quick Sort
# Solved
# Implement Quick Sort.

# Quick Sort is a divide-and-conquer sorting algorithm that works by partitioning an array into two smaller sub-arrays based on a pivot element. The elements less than the pivot go to the left sub-array and those greater go to the right sub-array. The algorithm then recursively sorts the sub-arrays.

# Solution:
# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def quic_sort(self, pairs: list[Pair]) -> list[Pair]:
        self.quicksort_helper(pairs, 0, len(pairs) - 1)
        return pairs

    def quicksort_helper(self, arr, s, e):
        if e - s + 1 <= 1:
            return

        p = arr[e]
        pointer = s

        for i in range(s, e):
            if arr[i].key < p.key:
                tmp = arr[pointer]
                arr[pointer] = arr[i]
                arr[i] = tmp
                pointer += 1

        arr[e] = arr[pointer]
        arr[pointer] = p

        self.quicksort_helper(arr, s, pointer - 1)
        self.quicksort_helper(arr, pointer + 1, e)


# time complexity = O(n)
# space complexity = O(n)
