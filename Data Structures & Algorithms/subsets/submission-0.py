class Solution:
    def myFun(self,arr,temp,result,index,n):
        if index>=n:
            result.append(temp[:])
            return 

        temp.append(arr[index]) 
        self.myFun(arr,temp,result,index+1,n)
        temp.pop()
        self.myFun(arr,temp,result,index+1,n)
        

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.myFun(nums,[],result,0,len(nums))
        return result