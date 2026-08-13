# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def myFun(self,root):
        if not root:
            return 

        temp=root.left
        root.left=self.myFun(root.right)
        root.right=self.myFun(temp)
        return root
            
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        return self.myFun(root)    