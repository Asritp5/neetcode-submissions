# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def myFun(self,root,result):
        if not root:
            return 0

        left=max(self.myFun(root.left,result),0)

        right=max(self.myFun(root.right,result),0)

        result[0]=max(result[0],left+right+root.val)
        
        return max(left+root.val,root.val+right,0)    

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[-math.inf,]
        self.myFun(root,res)
        return res[0]