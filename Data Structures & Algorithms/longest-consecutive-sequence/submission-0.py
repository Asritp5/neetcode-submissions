class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet=set(nums)

        count=max_count=0

        for num in nums:
            count=1
            x=num
            while x-1 in mySet:
                x=x-1
                count+=1

            max_count=max(max_count,count)

        return max_count          