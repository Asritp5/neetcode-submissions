class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)

        if n==1:
            return nums[0]

        if n==2:
            return max(nums)

        prev2,prev=nums[0],max(nums[0],nums[1])

        for i in range(2,n):
            val1=prev2+nums[i]
            val2=prev

            prev2,prev=prev,max(val1,val2)

        return prev        