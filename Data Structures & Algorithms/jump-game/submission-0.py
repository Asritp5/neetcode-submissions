class Solution:
    def canJump(self, nums: List[int]) -> bool:
        total=0
        n=len(nums)

        for i in range(n):
            if total<i:
                return False
            num=nums[i]
            total=max(total,nums[i]+i)

        return True    