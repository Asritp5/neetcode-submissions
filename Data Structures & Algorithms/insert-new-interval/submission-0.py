class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        intervals.sort()
        n=len(intervals)

        i=0
        while i<n:
            if intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
                i+=1
            else:
                break

        while i<n:
            if intervals[i][0]<=newInterval[1]:
                newInterval[0],newInterval[1]=min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])
                i+=1
            else:
                break

        res.append(newInterval)

        while i<n:
            res.append(intervals[i])
            i+=1

        return res    


                           