class Solution:
    def bfs(self,grid,i,j,m,n):
        queue=deque()
        queue.append((i,j))
        grid[i][j]=0
        dirs=[(-1,0),(0,-1),(0,1),(1,0)]
        while queue:
            x,y=queue.popleft()

            for x1,y1 in dirs:
                if 0<=x+x1<m and 0<=y+y1<n and grid[x+x1][y+y1]=="1":
                    grid[x+x1][y+y1]=0
                    queue.append((x+x1,y+y1))

    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        total=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    total+=1
                    self.bfs(grid,i,j,m,n)

        return total            