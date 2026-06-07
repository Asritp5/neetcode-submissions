class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict={}
        n=len(nums)

        for i in range(n):
            if target-nums[i] in myDict:
                return [myDict[target-nums[i]],i]
            myDict[nums[i]]=i

                