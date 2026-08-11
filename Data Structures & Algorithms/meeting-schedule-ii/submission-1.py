"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        intervals.sort(key=lambda x:x.start)    
        n=len(intervals)
        room=[intervals[0].end,]

        for i in range(1,n):
            start_time,end_time=intervals[i].start,intervals[i].end
            if start_time>=room[0]:
                heapq.heappop(room)
            heapq.heappush(room,end_time)

        return len(room)                