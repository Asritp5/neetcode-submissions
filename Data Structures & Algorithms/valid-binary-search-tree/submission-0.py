# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def myFun(self,root):
        if not root:
            return (True,math.inf,-math.inf)

        flag1,left1,right1=self.myFun(root.left)
        if not flag1:
            return False,-1,-1
        
        flag2,left2,right2=self.myFun(root.right)
        if not flag2:
            return False,-1,-1

        if right1<root.val<left2:
            return True,min(left1,root.val),max(right2,root.val)  
        return False,-1,-1      
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag,_,_=self.myFun(root)

        return flag