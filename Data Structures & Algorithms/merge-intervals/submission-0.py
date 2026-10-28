class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort()
        res=[]

        start,end=intervals[0][0],intervals[0][1]

        for i in range(1,n):
            if intervals[i][0]>end:
                res.append([start,end])
                start,end=intervals[i][0],intervals[i][1]
            else:
                end=max(end,intervals[i][1])

        res.append([start,end])

        return res    
         
