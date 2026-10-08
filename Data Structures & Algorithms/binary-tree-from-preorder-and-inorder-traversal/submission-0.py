# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def build(self,pre,inor,mydict,index,low,high,n):
        if low>high or index>=n:
            return None

        root_index=mydict[pre[index]]
        root=TreeNode(pre[index])

        if low!=high:
            root.left=self.build(pre,inor,mydict,index+1,low,root_index-1,n)    
            branch_len=root_index-low
            root.right=self.build(pre,inor,mydict,index+branch_len+1,root_index+1,high,n)    

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(inorder)
        
        if n==1:
            return TreeNode(inorder[0])

        myDict={}

        for i in range(n):
            myDict[inorder[i]]=i

        return self.build(preorder,inorder,myDict,0,0,n-1,n)    