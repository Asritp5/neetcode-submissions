class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[]
        suffix=[0]*n
        
        product=1
        for i in range(n):
            prefix.append(product)
            product*=nums[i]

        product=1
        for i in range(n-1,-1,-1):
            suffix[i]=product
            product*=nums[i]

        result=[]
        for i in range(n):
            result.append(prefix[i]*suffix[i])    
        return result    