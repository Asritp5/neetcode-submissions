# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def myFun(self,root,max_val):
        if not root:
            return 0

        count=0
        if root.val>=max_val:
            count=1
        
        count+=self.myFun(root.left,max(max_val,root.val))
        count+=self.myFun(root.right,max(max_val,root.val))
        return count        
    def goodNodes(self, root: TreeNode) -> int:
        return self.myFun(root,-101)