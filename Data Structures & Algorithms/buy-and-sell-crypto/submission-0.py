class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=max_profit=0
        n=len(prices)
        buy,sell=0,1

        while sell<n:
            profit=prices[sell]-prices[buy]

            max_profit=max(max_profit,profit)
            if profit<0:
                buy=sell

            sell+=1

        return max_profit        