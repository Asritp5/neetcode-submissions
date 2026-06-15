class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)

        result=[]
        for i in range(2**n):
            temp=[]
            for j in range(n):
                if i&(1<<j):
                    temp.append(nums[j])
            result.append(temp)

        return result            