class Solution:
    def myFun(self,board,visited,i,j,m,n,index,word,k):
        if index>=k:
            return True

        dirs=[(-1,0),(0,-1),(0,1),(1,0)]

        for x,y in dirs:
            x1,y1=x+i,y+j
            if 0<=x1<m and 0<=y1<n and visited[x1][y1]==False \
            and board[x1][y1]==word[index]:
                visited[x1][y1]=True
                if self.myFun(board,visited,x1,y1,m,n,index+1,word,k):
                    return True
                visited[x1][y1]=False
        return False            

    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        visited=[[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visited[i][j]=True
                    if self.myFun(board,visited,i,j,m,n,1,word,len(word)):
                        return True
                    visited[i][j]=False

        return False            
