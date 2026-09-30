class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)

        if n==1:
            return nums[0]
        elif n==2:
            return max(nums)
        else:
            val1=self.myFun(nums[:-1],n-1)
            val2=self.myFun(nums[1:],n-1)

            return max(val1,val2)
                
    def myFun(self,nums,n):
        prev2,prev=nums[0],max(nums[0],nums[1])

        for i in range(2,n):
            val1=prev2+nums[i]
            val2=prev

            prev2,prev=prev,max(val1,val2)

        return prev
