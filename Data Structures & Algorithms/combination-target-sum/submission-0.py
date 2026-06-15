class Solution:
    def myFun(self,nums,index,n,target,temp,result):
        if target==0:
            result.append(temp[:])
            return 

        if index>=n:
            return 

        if target<=1:
            return 

        if target>=nums[index]:
            temp.append(nums[index])
            self.myFun(nums,index,n,target-nums[index],temp,result)
            temp.pop()
        self.myFun(nums,index+1,n,target,temp,result)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]

        self.myFun(nums,0,len(nums),target,[],result)
        return result