class MedianFinder:

    def __init__(self):
        self.min_heap=[]
        self.max_heap=[]
        self.count_min=0
        self.count_max=0
        

    def addNum(self, num: int) -> None:
        if self.count_max>self.count_min:
            heapq.heappush(self.min_heap,num)
            self.count_min+=1
        else:
            heapq.heappush(self.max_heap,-num)
            self.count_max+=1

        while self.min_heap and self.max_heap and \
        -self.max_heap[0]>self.min_heap[0]:
            value1,value2=-heapq.heappop(self.max_heap),heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-value2)
            heapq.heappush(self.min_heap,value1)

    def findMedian(self) -> float:
        if (self.count_min+self.count_max)%2:
            return -self.max_heap[0]

        return (self.min_heap[0]-self.max_heap[0])/2            
        