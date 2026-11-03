class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        start,end=n-1,0

        total=gas[start]-cost[start]

        while start>end:
            if total<0:
                start-=1
                total+=gas[start]-cost[start]
            else:
                total+=gas[end]-cost[end]
                end+=1

        return start if total>=0 else -1    
