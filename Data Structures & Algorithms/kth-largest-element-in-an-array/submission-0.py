class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k==1:
            return max(nums)

        n=len(nums)
        heap=nums[:k]
        
        heapq.heapify(heap) 
        for i in range(k,n):
            num=nums[i]

            if num>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)
        return heap[0]                

