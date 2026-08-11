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

        time=[]
        for interval in intervals:
            time.append((interval.start,1))
            time.append((interval.end,-1))
        time.sort()

        total=max_val=0
        for event_time,count in time:
            total+=count
            max_val=max(max_val,total)

        return max_val                