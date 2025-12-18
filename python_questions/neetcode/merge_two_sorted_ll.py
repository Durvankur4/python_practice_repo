# Quesiton:

# Merge Two Sorted Linked Lists
# Solved
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
# The new list should be made up of nodes from list1 and list2.
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,5]
# Output: [1,1,2,3,4,5]
# Example 2:
# Input: list1 = [], list2 = [1,2]
# Output: [1,2]
# Example 3:
# Input: list1 = [], list2 = []
# Output: []
# Constraints:
# 0 <= The length of the each list <= 100.
# -100 <= Node.val <= 100


# Solution:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(list1: ListNode, list2: ListNode):
    d = ListNode()
    curr = d

    while list1 and list2:
        if list1.val < list2.val:

            curr.next = list1
            curr = list1
            list1 = list1.next

        else:
            curr.next = list2
            curr = list2
            list2 = list2.next

    curr.next = list1 if list1 else list2
    return d.next


# time complexity = O(n)
# space complexity = O(1)
