class Solution:
    def myFun(self,nums,index,target,dp):
        if index<0 or target<0:
            return False

        if dp[index][target]!=-1:
            return dp[index][target]    

        if target==0:
            dp[index][target]=True
            return dp[index][target]
        
        val1=False
        if nums[index]<=target:
            val1=self.myFun(nums,index-1,target-nums[index],dp)
        val2=self.myFun(nums,index-1,target,dp)

        dp[index][target]=val1 or val2
        return dp[index][target]

    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)

        sum_val=sum(nums)

        if sum_val%2:
            return False

        dp=[[-1]*(sum_val//2+1) for _ in range(n)]

        return self.myFun(nums,n-1,sum_val//2,dp)
