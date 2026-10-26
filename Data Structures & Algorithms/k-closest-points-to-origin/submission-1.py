class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n=len(points)
        point_data=[]
        
        for x,y in points:
            point_data.append((-(x*x+y*y)**0.5,x,y))
        
        heap=point_data[:k]
        heapq.heapify(heap)

        for i in range(k,n):
            if -heap[0][0]>-point_data[i][0]:
                heapq.heappop(heap)
                heapq.heappush(heap,point_data[i])

        res=[]
        for _,x,y in heap:
            res.append([x,y])
        return res
