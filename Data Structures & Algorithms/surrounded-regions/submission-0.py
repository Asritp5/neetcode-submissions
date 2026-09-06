class Solution:
    def bfs(self,x,y,m,n,board):
        queue=deque([(x,y)])
        dirs=[(-1,0),(0,1),(0,-1),(1,0)]
        while queue:
            i,j=queue.popleft()

            for x1,y1 in dirs:
                x2,y2=i+x1,j+y1
                if 1<=x2<m-1 and 1<=y2<n-1 and board[x2][y2]=="O":
                    board[x2][y2]="-1"
                    queue.append((x2,y2))

    def solve(self, board: List[List[str]]) -> None:
        m,n=len(board),len(board[0])

        queue=deque()
        for i in range(m):
            if board[i][0]=="O":
                self.bfs(i,0,m,n,board)

            if board[i][-1]=="O":
                self.bfs(i,n-1,m,n,board)

        for i in range(n):
            if board[0][i]=="O":
                self.bfs(0,i,m,n,board)

            if board[-1][i]=="O":
                self.bfs(m-1,i,m,n,board)

        
        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="-1":
                    board[i][j]="O"

            