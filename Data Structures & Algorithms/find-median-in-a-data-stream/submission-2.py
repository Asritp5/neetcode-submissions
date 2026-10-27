class MedianFinder:

    def __init__(self):
        self.min_heap=[]
        self.max_heap=[]
        self.count_min=0
        self.count_max=0
        

    def addNum(self, num: int) -> None:
        if self.count_max<=0 or -self.max_heap[0]>num:
            heapq.heappush(self.max_heap,-num)
            self.count_max+=1
        else:
            heapq.heappush(self.min_heap,num)
            self.count_min+=1

        
        if self.count_min<self.count_max:
                value=-heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap,value)
                self.count_min+=1
                self.count_max-=1
        if self.count_min>self.count_max:
                value=heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap,-value)
                self.count_min-=1
                self.count_max+=1
            
    def findMedian(self) -> float:
        if (self.count_min+self.count_max)%2:
            return -self.max_heap[0]

        return (self.min_heap[0]-self.max_heap[0])/2            
        