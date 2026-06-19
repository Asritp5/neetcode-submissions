class Solution:
    def myFun(self,temp,res,index,n,nums):
        if index>=n:
            res.add(tuple(sorted(temp)))
            return 

        temp.append(nums[index])
        self.myFun(temp,res,index+1,n,nums)
        temp.pop()
        
        self.myFun(temp,res,index+1,n,nums)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        self.myFun([],res,0,len(nums),nums)

        result=[]
        for tpl in res:
            result.append(list(tpl))

        return result     