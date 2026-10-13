class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)

        sum_val=sum(nums)

        if sum_val%2:
            return False

        prev=[False]*(sum_val//2+1)
        prev[0]=True

        for i in range(n):
            cur=[False]*(sum_val//2+1)
            for j in range(sum_val//2+1):
                if prev[j]==True:
                    cur[j]=True

                    if j+nums[i]<=sum_val//2:
                        cur[j+nums[i]]=True
            prev=cur            

        return cur[-1]
