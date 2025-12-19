# Quesiton:
# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and nxt. val is the value of the current node, and nxt is a pointer/reference to the nxt node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.


# Solution:
class ListNode:
    def __init__(self, val):
        self.val = val
        self.nxt = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.nxt
        while curr and index > 0:
            curr = curr.nxt
            index -= 1
        if index == 0 and curr and curr != self.tail:
            return curr.val
        return -1

    def addathead(self, val: int) -> None:
        node, nxt, prev = ListNode(val), self.head.nxt, self.head
        node.prev = prev
        node.nxt = nxt
        prev.nxt = node
        nxt.prev = node

    def addattail(self, val: int) -> None:
        node, nxt, prev = ListNode(val), self.tail, self.tail.prev
        node.prev = prev
        node.nxt = nxt
        prev.nxt = node
        nxt.prev = node

    def addatindex(self, index: int, val: int) -> None:
        curr = self.head.nxt
        while curr and index > 0:
            curr = curr.nxt
            index -= 1
        if curr and index == 0:
            node, nxt, prev = ListNode(val), curr, curr.prev
            node.prev = prev
            node.nxt = nxt
            prev.nxt = node
            nxt.prev = node

    def deleteatindex(self, index: int) -> None:
        curr = self.head.nxt
        while curr and index > 0:
            curr = curr.nxt
            index -= 1
        if curr and index == 0 and curr != self.tail:
            nxt, prev = curr.nxt, curr.prev
            nxt.prev = curr.prev
            prev.nxt = curr.nxt


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# time complexity = O(n)
# space complexity = O(n)
