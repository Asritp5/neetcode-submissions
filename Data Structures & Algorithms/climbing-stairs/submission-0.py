class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1

        prev2,prev=0,1

        for i in range(n):
            prev2,prev=prev,prev+prev2

        return prev    