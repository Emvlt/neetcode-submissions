class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        
        total = 0
        n = len(intervals)
        prevEnd = intervals[0][1]
        for i in range(1, n):
            # Check if interval overlaps with the previous
            if intervals[i][0] < prevEnd:
                prevEnd = min(prevEnd, intervals[i][1])
                total += 1
            else:
                prevEnd = intervals[i][1]
        return total