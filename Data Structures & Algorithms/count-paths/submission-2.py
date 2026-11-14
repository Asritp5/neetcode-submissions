class Solution:            
    def uniquePaths(self, m: int, n: int) -> int:
        prev=[1]*(n+1)
        
        for i in range(1,m):
            cur=[0]*(n+1)
            for j in range(1,n+1):
                cur[j]=prev[j]+cur[j-1]
            prev=cur

        return prev[-1]            