from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict=defaultdict(int)

        seen=set()
        for num in nums:
            myDict[num]+=1
            seen.add(num)

        queue=[]
        for key in seen:
            queue.append((-myDict[key],key))

        heapq.heapify(queue)

        res=[]
        while k>0:
            _,value=heapq.heappop(queue)
            k-=1
            res.append(value)

        return res    

            