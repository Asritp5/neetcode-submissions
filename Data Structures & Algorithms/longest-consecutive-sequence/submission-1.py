class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        index=0
        max_count=0
        count=1

        while index<n:
            prev=nums[index]
            
            index+=1
            while index<n and nums[index]==prev:
                index+=1

            if index<n and nums[index]==prev+1:
                count+=1
            else:
                max_count=max(max_count,count)
                count=1         

        return max_count    
