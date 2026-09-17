class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.heap.extend(nums[:k])
        heapq.heapify(self.heap)
        n=len(nums)
        self.cap=k

        for i in range(k,n):
            if nums[i]>self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap,nums[i])
        
    def add(self, val: int) -> int:
        if len(self.heap)<self.cap:
            heapq.heappush(self.heap,val)
        else:
            if self.heap[0]<val:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap,val)

        return self.heap[0]            
