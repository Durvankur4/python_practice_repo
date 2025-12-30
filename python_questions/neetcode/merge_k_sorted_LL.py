# Quesiton:

# Merge K Sorted Linked Lists
# Solved
# You are given an array of k linked lists lists, where each list is sorted in ascending order.

# Return the sorted linked list that is the result of merging all of the individual linked lists.

# Example 1:

# Input: lists = [[1,2,4],[1,3,5],[3,6]]

# Output: [1,1,2,3,3,4,5,6]
# Solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):  # noqa: A002
        self.val = val
        self.next = next


class Solution:
    def merge_k_lists(self, lists):
        if len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            lists[i] = self.mergeList(lists[i - 1], lists[i])

        return lists[-1]

    def merge_list(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


# time complexity = O(n)
# space complexity = O(n)
