class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)

        max_prod=max(nums)
        prod=nums[0]
        for i in range(1,n):
            prod*=nums[i]
            max_prod=max(max_prod,prod)
            if prod==0:
                prod=1
            
        prod=nums[-1]
        for i in range(n-2,-1,-1):
            prod*=nums[i]
            max_prod=max(max_prod,prod)                    
            if prod==0:
                prod=1
            
        return max_prod