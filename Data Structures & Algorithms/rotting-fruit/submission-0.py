from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count=rot_count=0
        m,n=len(grid),len(grid[0])
        queue=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((0,i,j))
                    rot_count+=1
                elif grid[i][j]==1:
                    fresh_count+=1

        if fresh_count==0:
            return 0

        if rot_count==0:
            return -1

        dirs=[(-1,0),(1,0),(0,-1),(0,1)]                        
        max_time=-1
        while queue:
            time,x,y=queue.popleft()
            max_time=time

            for x1,y1 in dirs:
                x2,y2=x+x1,y+y1

                if 0<=x2<m and 0<=y2<n and grid[x2][y2]==1:
                    grid[x2][y2]=2
                    fresh_count-=1
                    queue.append((time+1,x2,y2))
        
        if fresh_count==0:
            return max_time            
        return -1
