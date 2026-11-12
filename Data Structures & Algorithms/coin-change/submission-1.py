class Solution:
    def myFun(self,dp,coins,index1,index2):
        if index1<0 or index2<0:
            return math.inf

        if dp[index1][index2]!=-1:
            return dp[index1][index2]

        if index1==0:
            if index2%coins[0]==0:
                dp[0][index2]=index2//coins[0]
            else:
                dp[0][index2]=math.inf
            return dp[0][index2]    
            
        val1=self.myFun(dp,coins,index1-1,index2)
        val2=1+self.myFun(dp,coins,index1,index2-coins[index1])

        dp[index1][index2]=min(val1,val2)
        return dp[index1][index2]        
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0

        n=len(coins)
        coins.sort()

        dp=[[-1]*(amount+1)for _ in range(n)]
        self.myFun(dp,coins,n-1,amount)
        return dp[-1][-1] if dp[-1][-1]!=math.inf else -1