class Solution:
    def myFun(self,dp,index1,index2):
        if index1<0 or index2<0:
            return 0

        if dp[index1][index2]!=-1:
            return dp[index1][index2]

        if index1==0 and index2==0:
            dp[index1][index2]=1
            return dp[index1][index2]

        dp[index1][index2]=self.myFun(dp,index1-1,index2)+self.myFun(dp,index1,index2-1)

        return dp[index1][index2]
                
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*n for _ in range(m)]

        return self.myFun(dp,m-1,n-1)