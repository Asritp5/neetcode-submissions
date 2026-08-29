class Solution:
    def myFun(self,root,res):
        if not root:
            return

        self.myFun(root.left,res)
        res.append(root.val)
        self.myFun(root.right,res)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        self.myFun(root,res)

        return res[k-1]