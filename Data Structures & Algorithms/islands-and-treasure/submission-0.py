class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n=len(grid),len(grid[0])

        count=0
        queue=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    queue.append((i,j))
                elif grid[i][j]!=-1:
                    count+=1

        if count!=0:            
            dirs=[(-1,0),(0,-1),(0,1),(1,0)]
            while queue:
                x,y=queue.popleft()   

                for x1,y1 in dirs:
                    x2,y2=x+x1,y+y1
                    if 0<=x2<m and 0<=y2<n and grid[x2][y2]>grid[x][y]+1:
                        grid[x2][y2]=grid[x][y]+1
                        queue.append((x2,y2))


