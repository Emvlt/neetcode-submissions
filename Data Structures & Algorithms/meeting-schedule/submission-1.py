"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)

        intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(n-1):
            for j in range(i+1, n):
                if intervals[i].end > intervals[j].start:
                    return False 

        return True
