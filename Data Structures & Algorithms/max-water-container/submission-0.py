class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i,j=0,n-1

        max_water=0

        while i<j:
            capacity=min(heights[i],heights[j])*(j-i)
            max_water=max(max_water,capacity)

            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1

        return max_water            
        