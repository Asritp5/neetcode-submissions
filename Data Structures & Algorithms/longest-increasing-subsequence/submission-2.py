class Solution:
    def myFun(self,dp,arr,index1,index2,n):
        if index1>=n or index2>=n:
            return 0

        if dp[index1+1][index2]!=-1:
            return dp[index1+1][index2]

        val1=0
        if index1==-1 or arr[index1]<arr[index2]:
            val1=self.myFun(dp,arr,index2,index2+1,n)+1
        val2=self.myFun(dp,arr,index1,index2+1,n)
        
        dp[index1+1][index2]=max(val1,val2)
        return dp[index1+1][index2]          
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        dp=[[-1]*n for _ in range(n+1)]

        return self.myFun(dp,nums,-1,0,n)