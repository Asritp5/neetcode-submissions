class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)

        prev2,prev=cost[0],cost[1]

        for i in range(2,n):
            temp=min(prev2,prev)+cost[i]
            prev2,prev=prev,temp

        return min(prev,prev2)