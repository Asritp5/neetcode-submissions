class Solution:
    def nextSmaller(self,heights):
        n=len(heights)
        nse=[n]*n
        stack=[]

        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()

            if stack:
                nse[i]=stack[-1]

            stack.append(i)

        return nse

    def prevSmaller(self,heights):
        n=len(heights)
        pse=[-1]*n
        stack=[]

        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()

            if stack:
                pse[i]=stack[-1]

            stack.append(i)

        return pse
                    
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        nse,pse=self.nextSmaller(heights),self.prevSmaller(heights)
        max_area=0

        for i in range(n):
            area=(nse[i]-pse[i]-1)*heights[i]
            max_area=max(max_area,area)

        return max_area    