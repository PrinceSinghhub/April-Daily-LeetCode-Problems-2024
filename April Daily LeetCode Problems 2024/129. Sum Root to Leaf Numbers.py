# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def ans(self, root, Sum):

        if root == None:
            return 0

        Sum = Sum * 10 + root.val

        if root.left == None and root.right == None:
            return Sum

        return self.ans(root.left, Sum) + self.ans(root.right, Sum)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        return self.ans(root, 0)