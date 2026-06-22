class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total=-math.inf
        total=0
        for num in nums:
            total+=num

            max_total=max(max_total,total)
            total=max(0,total)

        return max_total    

        