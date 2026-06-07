from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict=defaultdict(int)
        n=len(nums)
        freq=[[] for _ in range(n+1)]
        seen=set()
        
        for num in nums:
            myDict[num]+=1
            seen.add(num)

        for key in seen:
            freq[myDict[key]].append(key)

        res=[]
        #print(freq)
        for i in range(n,-1,-1):
            while freq[i] and k>=0:
                res.append(freq[i].pop())
                k-=1
                
            if k<=0:
                return res
            
        return res    

            