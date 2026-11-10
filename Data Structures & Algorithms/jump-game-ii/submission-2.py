class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        jumps=0
        pos=max_jump=0
        
        for i in range(n-1):
            max_jump=max(max_jump,nums[i]+i)
            if pos==i:
                jumps+=1
                pos=max_jump
        return jumps        