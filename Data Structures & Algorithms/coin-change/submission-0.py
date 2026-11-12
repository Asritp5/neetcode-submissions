class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
            
        n=len(coins)
        coins.sort()

        dp=[[0]*(amount+1)for _ in range(n)]

        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=i//coins[0]
            else:
                dp[0][i]=math.inf

        for i in range(1,n):
            for j in range(1,amount+1):
                val=math.inf
                if j-coins[i]>=0:
                    val=dp[i][j-coins[i]]+1    
                dp[i][j]=min(dp[i-1][j],val)            

        return dp[-1][-1] if dp[-1][-1]!=math.inf else -1