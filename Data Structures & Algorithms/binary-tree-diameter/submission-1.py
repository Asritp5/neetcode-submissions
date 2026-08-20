# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def myFun(self,root,root_tree,res):
        if not root:
            return 0

        left=self.myFun(root.left,root_tree,res)
        right=self.myFun(root.right,root_tree,res)

        res[0]=max(res[0],left+right)
        return max(left,right)+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=[0,]
        self.myFun(root,root,res)        
        return res[0]