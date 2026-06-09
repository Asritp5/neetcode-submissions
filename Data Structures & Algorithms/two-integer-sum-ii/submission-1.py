class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        low,high=0,n-1

        while low<high:
            if nums[low]+nums[high]>target:
                high-=1

            elif nums[low]+nums[high]<target:
                low+=1

            else:
                return [low+1,high+1]

        return [-1,-1]            
                