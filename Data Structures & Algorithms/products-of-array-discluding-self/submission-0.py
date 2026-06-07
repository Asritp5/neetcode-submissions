class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        
        result=[]
        for i in range(n):
            product=1
            for j in range(n):
                if j==i:
                    continue

                product*=nums[j]
                if product==0:
                    break

            result.append(product)

        return result                