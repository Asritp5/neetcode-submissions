class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        
        row_0_col_0=row_0=False
        if matrix[0][0]==0:
            row_0_col_0=True

        if not row_0_col_0:    
            for i in range(1,m):
                if matrix[i][0]==0:
                    matrix[0][0]=0
                    break

            for i in range(1,n):
                if matrix[0][i]==0:
                    row_0=True
                    break

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        if row_0_col_0:
            for i in range(m):
                matrix[i][0]=0

            for i in range(n):
                matrix[0][i]=0

        elif matrix[0][0]==0:
            for i in range(m):
                matrix[i][0]=0

        elif row_0:
            for i in range(n):
                matrix[0][i]=0

        
        
            
            
        