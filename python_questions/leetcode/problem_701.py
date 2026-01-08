# # Quesiton:

# 701. Insert into a Binary Search Tree
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# # Solution:
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root :
#             return TreeNode(val)
#         if val > root.val:
#             root.right =  self.insertIntoBST(root.right,val)
#         else:
#             root.left =  self.insertIntoBST(root.left,val)
#         return root

# # time complexity = O(n)
# # space complexity = O(n
