class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        count=index=0
        product=1
        for i in range(n):
            num=nums[i]
            if num==0:
                count+=1
                index=i
            else:
                product*=num    

        if count>1:
            return [0]*n

        if count==1:
            return [0]*index+[product,]+[0]*(n-index-1)
            
        prefix=[]
        product=1
        for i in range(n):
            product*=nums[i]

            prefix.append(product)

        result=[]    

        for i in range(n):
            value1=1

            if i>0:
                value1=prefix[i-1]

            value2=prefix[-1]//prefix[i]
            result.append(value1*value2)

        return result    