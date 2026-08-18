# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def myFun(self,root):
        if not root:
            return True,0

        flag1,left=self.myFun(root.left)
        flag2,right=self.myFun(root.right)
        if not flag1 or not flag2:
            return False,-1

        if abs(left-right)>1:
            return False,-1
        return True,max(left,right)+1
            
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        flag,_=self.myFun(root)
        return flag    
