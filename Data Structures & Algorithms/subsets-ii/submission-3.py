class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)

        prev=ind=0
        res=[[]]

        for i in range(n):
            if i>=1 and nums[i]==nums[i-1]:
                ind=prev
            else:
                ind=0

            prev=len(res)
            for j in range(ind,prev):
                tmp=res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)

        return res               