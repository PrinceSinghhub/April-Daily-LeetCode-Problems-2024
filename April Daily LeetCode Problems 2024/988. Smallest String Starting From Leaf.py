# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans="~"
        self.traverse(root,[])
        return self.ans
    def traverse(self,root,path):
        if not root:
            return
        path.append(chr(root.val+97))
        if not root.left and not root.right:
            self.ans=min(self.ans,"".join(reversed(path)))
        self.traverse(root.left,path)
        self.traverse(root.right,path)
        path.pop()