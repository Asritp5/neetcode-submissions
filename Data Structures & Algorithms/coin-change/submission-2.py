class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        n=len(coins)
        coins.sort()

        prev=[]
        for i in range(amount+1):
            if i%coins[0]==0:
                prev.append(i//coins[0])
            else:
                prev.append(math.inf)

        for i in range(1,n):
            cur=[]
            for j in range(amount+1):
                val=math.inf
                if j-coins[i]>=0:
                    val=cur[j-coins[i]]+1    
                cur.append(min(prev[j],val))            
            prev=cur    
        
        return prev[-1] if prev[-1]!=math.inf else -1