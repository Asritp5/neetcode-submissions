from collections import deque
class Solution:
    def bfs(self,grid,i,j,m,n):
        queue=deque([(i,j),])

        grid[i][j]=0
        count=1
        dirs=[(-1,0),(0,-1),(0,1),(1,0)]
        while queue:
            x,y=queue.popleft()
            
            for x1,y1 in dirs:
                x2,y2=x+x1,y+y1
                if 0<=x2<m and 0<=y2<n and grid[x2][y2]==1:
                    grid[x2][y2]=0
                    queue.append((x2,y2))
                    count+=1
        return count            

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_count=0
        m,n=len(grid),len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    max_count=max(max_count,self.bfs(grid,i,j,m,n))
        return max_count            