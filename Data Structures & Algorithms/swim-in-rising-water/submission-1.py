class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dirs=[(-1,0),(0,-1),(0,1),(1,0)]

        queue=[(0,0,0)] #height,x,y
        max_time=grid[0][0]

        while queue:
            time,x,y=heapq.heappop(queue)

            max_time=max(max_time,time)

            if x==m-1 and y==n-1:
                return max_time

            for x1,y1 in dirs:
                x2,y2=x+x1,y+y1
                
                if 0<=x2<m and 0<=y2<n and grid[x2][y2]!=-1:    
                    heapq.heappush(queue,(max(grid[x2][y2],max_time),x2,y2))
                    grid[x2][y2]=-1

        return -1

