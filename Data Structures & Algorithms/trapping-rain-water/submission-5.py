class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        nge=[-1]*n
        pre=[]

        max_val=height[-1]
        for i in range(n-1,-1,-1):
            max_val=max(max_val,height[i])
            nge[i]=max_val

        max_val=height[0]
        for i in range(n):
            max_val=max(max_val,height[i])
            pre.append(max_val)

        total=0

        for i in range(n):
            if nge[i]!=-1 and pre[i]!=-1:
                total+=min(nge[i],pre[i])-height[i]    

        return total    