class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)

        for i in range(n//2):
            matrix[i],matrix[n-1-i]=matrix[n-1-i],matrix[i]

        for i in range(n):
            for j in range(i,n):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]    

              