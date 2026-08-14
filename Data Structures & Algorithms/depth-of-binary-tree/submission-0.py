# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def myFun(self,root):
        if not root:
            return 0

        h1=self.myFun(root.left)
        h2=self.myFun(root.right)

        return max(h1,h2)+1
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.myFun(root)    