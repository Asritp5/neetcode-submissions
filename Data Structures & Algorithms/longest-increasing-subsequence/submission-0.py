class Solution:
    def search(self,arr,key,n):
        low,high=0,n-1
        
        while low<=high:
            mid=(low+high)//2

            if arr[mid]<key:
                low=mid+1
            else:
                high=mid-1

        return low
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums) 
        arr=[nums[0],]
        length=1

        for i in range(1,n):
            key=nums[i]
            index=self.search(arr,key,length)    
            if index>=length:
                arr.append(key)
                length+=1
            else:
                arr[index]=key 

        return length           