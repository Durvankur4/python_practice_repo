# Quesiton:
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
# Example 1:
# Input: head = [0,1,2,3]
# Output: [3,2,1,0]
# Example 2:
# Input: head = []
# Output: []
# Constraints:
# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000


# Solution:
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def rev(head: ListNode):
    curr = head
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


# time complexity = O(n)
# space complexity = O(n)
