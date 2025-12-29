# Quesiton:
# Merge Sort
# Solved
# Implement Merge Sort.

# Merge Sort is a divide-and-conquer algorithm for sorting an array or list of elements. It works by recursively dividing the unsorted list into n sub-lists, each containing one element. Then, it repeatedly merges sub-lists to produce new sorted sub-lists until there is only one sub-list remaining.

# Objective:

# Given a list of key-value pairs, sort the list by key using Merge Sort. If two key-value pairs have the same key, maintain their relative order in the sorted list.


# Solution:
# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def merge_sort(self, pairs: list[Pair]) -> list[Pair]:
        return self.merge_sort_helper(pairs, 0, len(pairs) - 1)

    def merge_sort_helper(self, pairs, s, e) -> list[Pair]:
        if s >= e:  # if base case
            return pairs

        # middle of array
        m = (s + e) // 2

        # sort the left and right half
        self.merge_sort_helper(pairs, s, m)
        self.merge_sort_helper(pairs, m + 1, e)

        # merge sorted halfs
        self.merge(pairs, s, m, e)
        return pairs

    def merge(self, arr, s, m, e):
        # Copy the sorted left right half to L and R
        L = arr[s : m + 1]  # noqa: N806
        R = arr[m + 1 : e + 1]  # noqa: N806

        i, j, k = 0, 0, s  # index for the three arrays

        # merge the two sorted halfs into the oiriginal
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # one of the halfs have remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# time complexity = O(n)
# space complexity = O(n)
