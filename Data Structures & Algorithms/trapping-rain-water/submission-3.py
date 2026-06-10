class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        
        nge=[-1]*n
        pre=[]

        stack=[]
        for i in range(n-1,-1,-1):

            while stack and stack[-1]<=height[i]:
                stack.pop()

            if stack:
                nge[i]=stack[-1]
            
            if not stack:
                stack.append(height[i])

        stack=[]
        for i in range(n):

            while stack and stack[-1]<=height[i]:
                stack.pop()

            if stack:
                pre.append(stack[-1])
            else:
                pre.append(-1)

            if not stack:
                stack.append(height[i])

        total=0
        for i in range(n):
            if nge[i]!=-1 and pre[i]!=-1:
                total+=min(pre[i],nge[i])-height[i] 

        return total                   